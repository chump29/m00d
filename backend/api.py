#!.venv/bin/python

"""API Service"""

from dataclasses import dataclass
from functools import cache
from pathlib import Path
from sys import argv
from tomllib import load
from typing import TYPE_CHECKING

from box import Box, BoxError
from dotenv import dotenv_values
from fastapi import FastAPI
from peewee import AutoField, DateField, IntegerField, Model, SqliteDatabase
from playhouse.shortcuts import model_to_dict
from pydantic import BaseModel, ConfigDict, Field
from rich.console import Console
from rich.traceback import install as catch_exceptions
from uvicorn import run

if TYPE_CHECKING:
    from datetime import date
else:
    date = object  # pylint: disable=invalid-name

DEBUG = False

DB_PATH = "./db/"
DB_FILE = "m00d.db"

console = Console()
catch_exceptions()


if len(argv) > 1 and argv[1] != "--stop":
    try:
        PORT = int(argv[1])
    except ValueError as e:
        MSG = f"Invalid port: {argv[1]}"
        raise SystemExit(MSG) from e
else:
    try:
        PORT = int(Box(dotenv_values()).API_PORT)
    except (BoxError, ValueError) as e:
        MSG = "Invalid port"
        raise SystemExit(MSG) from e


class MoodDTO(BaseModel):
    """Mood domain model"""

    id: int | None = None
    mood: int = Field(ge=1, le=5)
    date: date
    model_config = ConfigDict(extra="forbid")


class Mood(Model):
    """m00d database model"""

    id = AutoField()
    mood = IntegerField()
    date = DateField(unique=True)

    @dataclass
    class Meta:
        """Metadata"""

        database = SqliteDatabase(DB_PATH + DB_FILE, pragmas={"journal_mode": "wal"})


def log(msg: str, info: str = "") -> None:
    """Log to console"""
    s = f"[bold green]{msg}[/bold green]"
    if info:
        s = f"{s}: [cyan]{info}[/cyan]"
    console.log(s)


if not Path(DB_PATH).exists():
    if DEBUG:
        log("Creating path", DB_PATH)
    Path(DB_PATH).mkdir(parents=True)

if not Path(DB_PATH + DB_FILE).exists():
    if DEBUG:
        log("Creating database", DB_FILE)
    Mood.create_table()
elif DEBUG:
    log("Using database", DB_PATH + DB_FILE)

api = FastAPI(
    docs_url="/api/docs", openapi_url="/api/openapi.json", redoc_url="/api/redoc"
)


@cache
@api.get("/api/version")
def get_version() -> str | None:
    """Return version"""
    try:
        with Path("pyproject.toml").open("rb") as pyproject:
            return Box(load(pyproject)).project.version
    except Exception:  # pylint: disable=broad-exception-caught
        console.print_exception()
        return None


@api.get("/api/get", response_model=list[MoodDTO] | None)
def get() -> list[MoodDTO] | None:
    """Get all moods"""
    try:
        if DEBUG:
            log("Getting rows", str(Mood.select().count(None)))
        return list(Mood.select().order_by(Mood.date.asc()).dicts()) or None
    except Exception:  # pylint: disable=broad-exception-caught
        console.print_exception()
        return None


@api.get("/api/get/{pk}", response_model=MoodDTO | None)
def get_one(pk: int) -> MoodDTO | None:
    """Get mood by ID"""
    try:
        if DEBUG:
            log("Getting row id", str(pk))
        return Mood.get_by_id(pk) or None
    except Exception:  # pylint: disable=broad-exception-caught
        console.print_exception()
        return None


@api.get("/api/get_by_date/{d}", response_model=MoodDTO | None)
def get_by_date(d: date) -> MoodDTO | None:
    """Get mood by date"""
    try:
        if DEBUG:
            log("Getting row by date", str(d))
        return Mood.get(Mood.date == d) or None
    except Exception:  # pylint: disable=broad-exception-caught
        return None


@api.post("/api/add", response_model=MoodDTO | None)
def add(mood: MoodDTO) -> MoodDTO | None:
    """Add mood"""
    try:
        if DEBUG:
            log("Adding row", f"mood={mood.mood} date={mood.date}")
        d = get_by_date(mood.date)
        if d and d.id:
            if DEBUG:
                log("➪ Updating instead of adding")
            return update(d.id, mood)
        m = Mood.create(mood=mood.mood, date=mood.date)
        return MoodDTO.model_validate(model_to_dict(m)) if m else None
    except Exception:  # pylint: disable=broad-exception-caught
        console.print_exception()
        return None


@api.put("/api/update/{pk}", response_model=MoodDTO | None)
def update(pk: int, mood: MoodDTO) -> MoodDTO | None:
    """Update mood by ID"""
    try:
        if DEBUG:
            log("Updating row id", str(pk))
        return (
            get_one(pk)
            if Mood.update(mood=mood.mood).where(Mood.id == pk).execute() > 0
            else None
        )
    except Exception:  # pylint: disable=broad-exception-caught
        console.print_exception()
        return None


@api.delete("/api/delete/{pk}")
def delete(pk: int) -> bool:
    """Delete mood by ID"""
    try:
        if DEBUG:
            log("Deleting row id", str(pk))
        menu = Mood.get(Mood.id == pk)
        menu.delete_instance()
    except Exception:  # pylint: disable=broad-exception-caught
        console.print_exception()
        return False
    return True


if __name__ == "__main__":
    log("✨ Running local server...")
    run(app="api:api", host="0.0.0.0", port=PORT, reload=True)  # noqa: S104

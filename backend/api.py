#!.venv/bin/python

"""API Service"""

from dataclasses import dataclass
from datetime import date
from html import escape
from os import environ, getenv, makedirs, path
from tomllib import load

from fastapi import FastAPI
from peewee import AutoField, DateField, IntegerField, Model, SqliteDatabase
from pydantic import BaseModel
from uvicorn import run

DB_PATH = "./db/"
DB_FILE = "m00d.db"

DEBUG = True


class MoodDTO(BaseModel):
    """Mood data model"""

    id: int | None = None
    mood: int
    date: date  # YYYY-MM-DD


class Mood(Model):
    """m00d DB model"""

    id = AutoField()
    mood = IntegerField()
    date = DateField(unique=True)

    @dataclass
    class Meta:
        """Metadata"""

        database = SqliteDatabase(DB_PATH + DB_FILE, pragmas={"journal_mode": "wal"})


if not path.exists(DB_PATH):
    if DEBUG:
        print(f"Creating path: {DB_PATH}")
    makedirs(DB_PATH)

if not path.exists(DB_PATH + DB_FILE):
    if DEBUG:
        print(f"Creating database: {DB_FILE}")
    Mood.create_table()

api = FastAPI(
    docs_url="/api/docs", openapi_url="/api/openapi.json", redoc_url="/api/redoc"
)


@api.get("/api/version")
def get_version() -> str | None:
    """Returns version"""
    try:
        version = getenv("BACKEND_VERSION")
        if not version:
            with open(file="pyproject.toml", mode="rb") as pyproject:
                version = load(pyproject)["project"]["version"]
                environ["BACKEND_VERSION"] = version
        return escape(str(version))
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(e)
        return None


@api.get("/api/get", response_model=list[MoodDTO] | None)
def get() -> list[MoodDTO] | None:
    """Get all moods"""
    try:
        if DEBUG:
            print(f"Getting rows: {Mood.select().count(None)}")
        return list(Mood.select().order_by(Mood.date.asc()).dicts()) or None
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(e)
        return None


@api.get("/api/get/{pk}", response_model=MoodDTO | None)
def get_one(pk: int) -> MoodDTO | None:
    """Get mood by ID"""
    try:
        if DEBUG:
            print(f"Getting row id: {pk}")
        return Mood.get_by_id(pk) or None
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(e)
        return None


@api.get("/api/get_by_date/{d}", response_model=MoodDTO | None)
def get_by_date(d: date) -> MoodDTO | None:
    """Get mood by date"""
    try:
        if DEBUG:
            print(f"Getting row by date: {d}")
        return Mood.get(Mood.date == d) or None
    except Exception:  # pylint: disable=broad-exception-caught
        return None


@api.post("/api/add", response_model=MoodDTO | None)
def add(mood: MoodDTO) -> MoodDTO | None:
    """Add mood"""
    try:
        if DEBUG:
            print(f"Adding row: mood={mood.mood}, date={mood.date}")
        d = get_by_date(mood.date)
        if d and d.id:
            return update(d.id, mood)
        return Mood.create(mood=mood.mood, date=mood.date) or None
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(e)
        return None


@api.put("/api/update/{pk}", response_model=MoodDTO | None)
def update(pk: int, mood: MoodDTO) -> MoodDTO | None:
    """Update mood by ID"""
    try:
        if DEBUG:
            print(f"Updating row id: {pk}")
        return (
            get_one(pk)
            if Mood.update(mood=mood.mood).where(Mood.id == pk).execute() > 0
            else None
        )
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(e)
        return None


@api.delete("/api/delete/{pk}")
def delete(pk: int) -> bool:
    """Delete mood by ID"""
    try:
        if DEBUG:
            print(f"Deleting row id: {pk}")
        menu = Mood.get(Mood.id == pk)
        menu.delete_instance()
        return True
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(e)
        return False


if __name__ == "__main__":
    run(app="api:api", host="0.0.0.0", port=5558, reload=True)

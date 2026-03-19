#!.venv/bin/python

# pylint: disable=C0116,E0102,E1102
# pyright: reportCallIssue=false, reportRedeclaration=false
# ruff: noqa: D103, F811

"""CRUD tests"""

from datetime import date
from secrets import randbelow
from typing import TYPE_CHECKING

from api import MoodDTO, get, get_one, update  # pylint: disable=E0401
from behave import given, then, when

if TYPE_CHECKING:
    from behave.runner import Context
else:
    Context = object

DATE = date(1111, 11, 11)


@given("that a user wants a mood by date")
def step_impl(context: Context) -> None:
    assert context.mood, "Invalid mood data"


@when("/get_by_date API endpoint is called")
def step_impl(context: Context) -> None:
    assert context.failed is not True, "/get_by_date call failed"


@then("mood data is returned")
def step_impl(context: Context) -> None:
    assert context.mood, "Invalid query results"


@then("the date matches")
def step_impl(context: Context) -> None:
    assert context.mood.date == DATE, "Date invalid"


@then("it can be updated")
def step_impl(context: Context) -> None:
    rnd = randbelow(2) + 4  # 4-5
    m = update(context.mood.id, MoodDTO(mood=rnd, date=DATE))
    assert m and m.mood == rnd, "Could not update mood"  # noqa: PT018
    m = get_one(context.mood.id)  # refetch
    assert (  # noqa: PT018
        m and m.id == context.mood.id
    ), "Could not get updated mood data"


@given("that a user wants all moods")
def step_impl(context: Context) -> None:
    context.mood = get()


@when("/get API endpoint is called")
def step_impl(context: Context) -> None:
    assert context.failed is not True, "/get call failed"


@then("all mood data is returned")
def step_impl(context: Context) -> None:
    assert context.mood, "Invalid query results"


@then("there is at least one row")
def step_impl(context: Context) -> None:
    assert len(context.mood) > 0, "Invalid row count"

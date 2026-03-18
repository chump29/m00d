#!.venv/bin/python

# pylint: skip-file
# type: ignore

from behave import given, then, when
from datetime import date
from random import randint

from api import get, get_one, MoodDTO, update

DATE = date(1111, 11, 11)


@given("that a user wants a mood by date")
def step_impl(context):
    assert context.mood, "Invalid mood data"


@when("/get_by_date API endpoint is called")
def step_impl(context):
    assert context.failed is not True, "/get_by_date call failed"


@then("mood data is returned")
def step_impl(context):
    assert context.mood, "Invalid query results"


@then("the date matches")
def step_impl(context):
    assert context.mood.date == DATE, "Date invalid"


@then("it can be updated")
def step_impl(context):
    rnd = randint(4, 5)
    assert (
        update(context.mood.id, MoodDTO(mood=rnd, date=DATE)).mood == rnd
    ), "Could not update mood"
    assert (
        get_one(context.mood.id).id == context.mood.id
    ), "Could not get updated mood data"  # refetch


@given("that a user wants all moods")
def step_impl(context):
    context.mood = get()


@when("/get API endpoint is called")
def step_impl(context):
    assert context.failed is not True, "/get call failed"


@then("all mood data is returned")
def step_impl(context):
    assert context.mood, "Invalid query results"


@then("there is at least one row")
def step_impl(context):
    assert len(context.mood) > 0, "Invalid row count"

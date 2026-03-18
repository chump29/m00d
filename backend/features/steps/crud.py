#!.venv/bin/python

# pylint: skip-file
# type: ignore

from behave import given, then, when
from datetime import date
from random import randint

from api import add, delete, get_by_date, MoodDTO, update

DATE = date(1111, 11, 11)


@given("that a user wants their mood by date")
def step_impl(context):
    mood = get_by_date(DATE)
    if mood:
        delete(mood.id)

    context.mood = add(MoodDTO(mood=randint(1, 2), date=DATE))
    assert context.mood, "Could not add mood"


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
    delete(context.mood.id)

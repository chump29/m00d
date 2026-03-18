#!.venv/bin/python

# pylint: skip-file
# type: ignore

from datetime import date
from random import randint

from api import add, delete, get_by_date, MoodDTO

DATE = date(1111, 11, 11)


def before_feature(context, _):
    mood = get_by_date(DATE)
    if mood:  # clean up any old data
        delete(mood.id)
    context.mood = add(MoodDTO(mood=randint(1, 2), date=DATE))
    assert context.mood, "Could not add mood data"


def after_feature(context, _):
    assert delete(context.mood.id), "Could not delete mood data"

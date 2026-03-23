#!.venv/bin/python

# pylint: disable=C0116
# ruff: noqa: D103

"""Environment setup"""

from datetime import date
from secrets import randbelow
from typing import TYPE_CHECKING

from api import MoodDTO, add, delete, get_by_date  # pylint: disable=E0401

if TYPE_CHECKING:
    from behave.model import Feature
    from behave.runner import Context
else:
    Feature = object
    Context = object

DATE = date(1111, 11, 11)


def before_feature(context: Context, feature: Feature) -> None:
    if "crud" not in feature.tags:
        return
    mood = get_by_date(DATE)
    if mood and mood.id:  # * clean up any old data
        delete(mood.id)
    context.mood = add(MoodDTO(mood=randbelow(2) + 1, date=DATE))  # * 1-2
    assert context.mood, "Could not add mood data"


def after_feature(context: Context, feature: Feature) -> None:
    if "crud" not in feature.tags:
        return
    assert delete(context.mood.id), "Could not delete mood data"

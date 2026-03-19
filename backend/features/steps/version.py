#!.venv/bin/python

# pylint: disable=C0116,E0102,E1102
# pyright: reportCallIssue=false, reportRedeclaration=false
# ruff: noqa: D103, F811

"""Version tests"""

from pathlib import Path
from tomllib import load
from typing import TYPE_CHECKING

from api import get_version  # pylint: disable=E0401
from behave import given, then, when

if TYPE_CHECKING:
    from behave.runner import Context
else:
    Context = object


@given("a request for the API version")
def step_impl(context: Context) -> None:
    with Path("pyproject.toml").open("rb") as pyproject:
        context.real_version = load(pyproject)["project"]["version"]


@when("/version API endpoint is called")
def step_impl(context: Context) -> None:
    context.version = get_version()
    assert context.failed is not True, "/version call failed"


@then("version is returned")
def step_impl(context: Context) -> None:
    assert context.real_version == context.version, "Invalid version"


@then("version is cached")
def step_impl(_: Context) -> None:
    get_version()
    get_version()
    v = get_version.cache_info()
    assert v.hits == 2 and v.misses == 1, "Version not cached"  # noqa: PT018, PLR2004

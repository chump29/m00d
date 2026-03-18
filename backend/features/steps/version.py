#!.venv/bin/python

# pylint: skip-file
# type: ignore

from behave import given, then, when
from tomllib import load

from api import get_version


@given("a request for the API version")
def step_impl(context):
    with open(file="pyproject.toml", mode="rb") as pyproject:
        context.real_version = load(pyproject)["project"]["version"]


@when("/version API endpoint is called")
def step_impl(context):
    context.version = get_version()
    assert context.failed is not True, "/version call failed"


@then("version is returned")
def step_impl(context):
    assert context.real_version == context.version, "Invalid version"


@then("version is cached")
def step_impl(_):
    get_version()
    get_version()
    v = get_version.cache_info()
    assert v.hits == 2 and v.misses == 1, "Version not cached"

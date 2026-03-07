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
    print(context.version)
    assert context.real_version == context.version, "Invalid version"

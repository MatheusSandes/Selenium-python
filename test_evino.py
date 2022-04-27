import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

scenarios("../../features/clinic_doctor.feature")

global driver
driver = webdriver.Firefox()

@pytest.fixture()
def setup():
    driver.get("https://www.evino.com.br/")
    driver.maximize_window()


@given(parsers.parse("one cart with "{number}" wines"))
def clinic_logged(number):
    """"""

@when("user checks the cart")
def when():
    """"""

@then(parsers.parse("must have "{number}" evino dropper in the cart at no additional cost"))
def then(number):
    "uiewch"
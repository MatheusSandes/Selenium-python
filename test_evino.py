import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string
from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

scenarios("./evino_scenarios.feature")
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def generate_email():
    name = ""
    for i in range(1, 9):
        name = name + "".join(random.choice(string.ascii_lowercase))
    return name + "@gmail.com"

@pytest.fixture()
def setup():
    driver.get("https://www.evino.com.br/")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.NAME, "user").click()
    driver.find_element(By.NAME, "user").send_keys(generate_email())
    driver.find_element(By.XPATH, "//button[contains(.,\'Entrar\')]").click()
    driver.execute_script("window.scrollTo(0, 800)") 
    time.sleep(3)


@given(parsers.parse('one cart with "{number}" wines'))
def one_cart_with_n_wines(setup, number):
    """Add wines into cart"""
    driver.find_element(By.XPATH, '//div[1]/div[1]/div[1]/a[1]/div[3]/figure[1]').click()
    time.sleep(3)
    i = 1
    global winePrice
    winePrice = driver.find_element(By().XPATH, '//body/div[@id=\'app\']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[5]/div[1]/div[1]/p[2]').text
    while i < int(number):
        driver.find_element(By.CLASS_NAME, 'ev-plus').click()
        i+=1
    driver.find_element(By.XPATH, "//button[1]/div[2]").click()

@when(parsers.parse('and with "{number}" wines of another type'))
def and_with_n_wines_of_another_type():
    """"""

@when("user checks the cart")
def user_checks_the_cart():
    """Open the cart"""
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='BuyBox']/div[1]/a[1]/button[1]").click()

@then(parsers.parse('must have "{number}" evino cut drops in the cart at no additional cost'))
def must_have_n_evino_cut_drops_in_the_cart(number):
    driver.find_element(By.XPATH)
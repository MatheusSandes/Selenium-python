import pytest
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable,
    visibility_of_element_located
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string
import re
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
wait = WebDriverWait(driver, 10)

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

def add_wine_to_cart(number):
    time.sleep(3)
    i = 1
    wait.until(
            element_to_be_clickable((By.CLASS_NAME, 'ev-plus')),'Element not found'
        )
    while i < int(number):
        driver.find_element(By.CLASS_NAME, 'ev-plus').click()
        i+=1

    element = driver.find_elements(By.XPATH, "//button[1]/div[2]") 
    if len(element) > 0: 
        driver.find_element(By.XPATH, "//button[1]/div[2]").click() 
    else: 
        driver.find_element(By.XPATH, "//div[contains(text(),'Adicionar')]").click()

@given(parsers.parse('one cart with "{number}" wines'))
def one_cart_with_n_wines(setup, number):
    """Add wines into cart"""
    driver.find_element(By.XPATH, '//div[1]/div[1]/div[1]/a[1]/div[3]/figure[1]').click()
    add_wine_to_cart(number)

@when(parsers.parse('and with "{number}" wines of another type'))
def and_with_n_wines_of_another_type(number):
    """Add wines into cart"""
    driver.find_element(By.XPATH, '//div[@class="Media__figure"]').click()
    driver.find_element(By.XPATH, '//div[2]/div[1]/div[1]/a[1]/div[3]/figure[1]').click()
    add_wine_to_cart(number)

@when("user checks the cart")
def user_checks_the_cart():
    """Open the cart"""
    driver.find_element(By.XPATH, "//button[contains(text(),'Não, obrigado')]").click()
    wait.until(
            element_to_be_clickable((By.XPATH, "//div[@class='CartNavigation']")),'Element not found'
        )
    driver.find_element(By.XPATH, "//div[@class='CartNavigation']").click()    

@then(parsers.parse('must have "{number}" evino cut drops in the cart at no additional cost'))
def must_have_n_evino_cut_drops_in_the_cart(number):
    wait.until(
            visibility_of_element_located((By.XPATH, "//p[contains(text(),'"+number+"un. grátis')]")),'Element not found'
        )
    text = driver.find_element(By.XPATH, "//p[contains(text(),'"+number+"un. grátis')]").text
    assert text == number+"un. grátis"
    total = driver.find_element(By.XPATH, "//div[@class='CartPriceWrapper']").text
    number = re.findall('[0-9]*,[0-9]*',total)
    assert "R$"+number[0] == driver.find_element(By.XPATH, "//div[@class='SummaryPrice']//p[2]").text

@then(parsers.parse('the number on the cart logo must have be "{number}"'))
def the_number_on_the_cart_logo_must_have_be(number):
    total = driver.find_element(By.XPATH, "//span[@class='CartNavigation__quantity']").text
    assert int(total) == int(number)

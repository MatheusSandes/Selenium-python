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

scenarios("./login_and_register_scenarios.feature")
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)

def generate_email():
    name = ""
    for i in range(1, 9):
        name = name + "".join(random.choice(string.ascii_lowercase))
    return name + "@gmail.com"

def generate_cpf():                                                        
    cpf = [random.randint(0, 9) for x in range(9)]                              
                                                                               
    for _ in range(2):                                                          
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
                                                                                
        cpf.append(11 - val if val > 1 else 0)                                  
                                                                                
    return '%s%s%s%s%s%s%s%s%s%s%s' % tuple(cpf)

def register_form(name, cpf, num, email, phone, password):
    driver.find_element(By.ID, ":r2:").click()
    driver.find_element(By.ID, ":r2:").send_keys(name)
    driver.find_element(By.ID, ":r3:").click()
    driver.find_element(By.ID, ":r3:").send_keys(cpf)
    driver.find_element(By.ID, ":r4:").click()
    driver.find_element(By.ID, ":r4:").send_keys(num)
    driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root").click()
    driver.find_element(By.ID, ":r5:").click()
    driver.find_element(By.ID, ":r5:").send_keys(email)
    driver.find_element(By.ID, ":r6:").click()
    driver.find_element(By.ID, ":r6:").send_keys(phone)
    driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained").click()
    driver.find_element(By.ID, ":r7:").click()
    driver.find_element(By.ID, ":r7:").send_keys(password)
    driver.find_element(By.ID, ":r8:").click()
    driver.find_element(By.ID, ":r8:").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained").click()

def setup():
    driver.get("https://proap-ufba.netlify.app/")
    driver.maximize_window()

@given("user at register page")
def user_at_register_page():
    """Add wines into cart"""
    setup()
    driver.find_element(By.LINK_TEXT, "Cadastre-se").click()

@when("fill the register form")
def fill_the_register_form():
    global email 
    email = generate_email()
    register_form("Matheus Sandes", generate_cpf(), "12345", email, "71999999999", "0987654321")

@when("fill the register form with missing fields")
def fill_the_register_form_with_missing_fields():
    global email 
    email = generate_email()
    driver.find_element(By.ID, ":r2:").click()
    driver.find_element(By.ID, ":r2:").send_keys("")
    driver.find_element(By.ID, ":r3:").click()
    driver.find_element(By.ID, ":r3:").send_keys("")
    driver.find_element(By.ID, ":r4:").click()
    driver.find_element(By.ID, ":r4:").send_keys("1111")
    driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root").click()

@when("fill the register form with invalid fields")
def fill_the_register_form_with_invalid_fields():
    global email 
    email = generate_email()
    driver.find_element(By.ID, ":r2:").click()
    driver.find_element(By.ID, ":r2:").send_keys("Matheus Sandes")
    driver.find_element(By.ID, ":r3:").click()
    driver.find_element(By.ID, ":r3:").send_keys("09876543210")
    driver.find_element(By.ID, ":r4:").click()
    driver.find_element(By.ID, ":r4:").send_keys("11111")
    driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root").click()

@then("the user must be registered")
def the_user_must_be_registered():
    driver.get("https://proap-ufba.netlify.app/")
    driver.find_element(By.ID, ":r0:").click()
    driver.find_element(By.ID, ":r0:").send_keys("matheus_sandes@hotmail.com")
    driver.find_element(By.ID, ":r1:").click()
    driver.find_element(By.ID, ":r1:").send_keys("0987654321")
    driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root").click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, "//h4[contains(.,\'Minhas solicitações\')]")

@then("the system must show an error")
def the_system_must_show_an_error():
    n = driver.find_elements(By.XPATH, "//p[contains(.,'Campo obrigatório')]").__len__()
    assert n == 2

@then("the system must show an invalid field error")
def the_system_must_show_an_invalid_field_error():
    time.sleep(1)
    n = driver.find_elements(By.XPATH, "//p[contains(.,'CPF inválido')]").__len__()
    assert n == 1

@given("user at login page")
def user_at_login_page():
    driver.find_element(By.NAME, "username").click()

@when("fill the login form as admin user")
def fill_the_form_as_admin_user():
    driver.find_element(By.NAME, "username").send_keys("matheus_sandes@hotmail.com")
    driver.find_element(By.NAME, "username").click()
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys("0987654321")
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root").click()

@then("user should be logged in as admin")
def user_should_be_logged_in_as_admin():
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//h4[contains(.,\'Minhas solicitações\')]")
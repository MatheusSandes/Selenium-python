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

scenarios("./solicitation.feature")
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)

def setup():
    driver.get("https://proap-ufba.netlify.app/")
    driver.maximize_window()

@given("user at solicitation page")
def user_at_solicitation_page():
    """Add wines into cart"""
    setup()
    driver.find_element(By.NAME, "username").send_keys("matheus_sandes@hotmail.com")
    driver.find_element(By.NAME, "username").click()
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys("0987654321")
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.XPATH, "//*[@id=\"root\"]/div[2]/div/div/form/button").click()

@when("fill the register form")
def fill_the_register_form():
    time.sleep(2)
    driver.find_element(By.XPATH, "(//button[@type=\'button\'])[4]").click()
    time.sleep(1)
    driver.find_element(By.NAME, "email").click()
    driver.find_element(By.NAME, "email").send_keys("matheus_sandes@hotmail.com")
    driver.find_element(By.NAME, "nomeCompleto").send_keys("Nome")
    driver.find_element(By.NAME, "titulo").send_keys("Tituulo")
    driver.find_element(By.NAME, "doi").send_keys("DOI")
    driver.find_element(By.NAME, "autores").send_keys("co-autores")
    driver.find_element(By.NAME, "alunoPGCOMP").click()
    driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    driver.find_element(By.XPATH, "(//input[@name=\'solicitacaoApoio\'])[2]").click()
    driver.find_element(By.NAME, "valorSolicitado").click()
    driver.find_element(By.NAME, "valorSolicitado").send_keys("111")
    driver.find_element(By.XPATH, "(//input[@name=\'solicitacaoAuxilioOutrasFontes\'])[2]").click()

    driver.find_element(By.NAME, "nomeAgenciaFomento").click()
    driver.find_element(By.NAME, "nomeAgenciaFomento").send_keys("111")
    driver.find_element(By.NAME, "valorSolicitadoAgenciaFomento").click()
    driver.find_element(By.NAME, "valorSolicitadoAgenciaFomento").send_keys("111")
    driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()

    driver.find_element(By.NAME, "dataInicio").send_keys("02022022")
    driver.find_element(By.NAME, "dataFim").send_keys("03022022")
    driver.find_element(By.NAME, "linkHomepage").click()
    driver.find_element(By.NAME, "linkHomepage").send_keys("link")
    driver.find_element(By.NAME, "cidade").click()
    driver.find_element(By.NAME, "cidade").send_keys("cidade")
    driver.find_element(By.NAME, "pais").send_keys("pais")
    driver.find_element(By.NAME, "valorInscricao").click()
    driver.find_element(By.NAME, "valorInscricao").send_keys("11")
    driver.find_element(By.NAME, "cartaAceite").click()
    driver.find_element(By.NAME, "cartaAceite").send_keys("carta")
    driver.find_element(By.XPATH, "//*[@id=\"stepper-form\"]/div[1]/div/div[3]/div").click()
    driver.find_element(By.XPATH, "//*[@id=\"menu-qualis\"]/div[3]/ul/li[2]").click()
    driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained").click()
    driver.find_element(By.NAME, "aceiteFinal").click()
    driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    driver.find_element(By.CSS_SELECTOR, ".MuiIconButton-edgeStart path").click()
    driver.find_element(By.XPATH, "//span[contains(.,\'Página Inicial\')]").click()

@then("the user must be registered")
def the_user_must_be_registered():
    message = driver.find_element(By.CSS_SELECTOR, ".Toastify__toast-body > div:nth-child(2)").text
    assert message == "ds"

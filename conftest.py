import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome()
    browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def login(driver):
    # driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    driver.find_element(By.XPATH, './/input[@name="name"]').send_keys('asyadambish7000@yandex.ru')
    driver.find_element(By.XPATH, './/input[@name="Пароль"]').send_keys('253579')
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    # WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    return driver

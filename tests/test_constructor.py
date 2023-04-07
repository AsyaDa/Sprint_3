from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from locator import Locators


class TestSectionInConstructor:
    def test_go_to_toppings(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.account_button))
        element = driver.find_element(By.XPATH, ".//h2[text()='Начинки']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        a = driver.find_element(*Locators.current_section).text
        assert a == "Начинки"

    def test_go_to_sauces(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.account_button))
        element = driver.find_element(By.XPATH, ".//h2[text()='Соусы']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        a = driver.find_element(*Locators.current_section).text
        assert a == "Соусы"

    def test_go_to_bun(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.account_button))
        element = driver.find_element(By.XPATH, ".//h2[text()='Булки']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        a = driver.find_element(*Locators.current_section).text
        assert a == "Булки"
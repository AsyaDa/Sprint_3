#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locators


class TestLogout:
    def test_logout(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.place_order_button))
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Выход']"))).click() #ждем и кликаем на кнопку Выход
        a = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.login_button_on_entry_page)) #ждем пока появится кнопка Войти
        assert a


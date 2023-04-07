from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locators


class TestGoToProfile:
    def test_go_to_personal_account(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.place_order_button))
        driver.find_element(*Locators.account_button).click()
        a = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//a[@href='/account/profile']"))).text
        assert a == "Профиль"

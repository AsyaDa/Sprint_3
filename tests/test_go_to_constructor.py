from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locators


class TestGoToConstructor:
    def test_go_to_constructor_by_button(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.account_button)).click()
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
        a = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.make_burger_header))
        assert a

    def test_go_to_constructor_by_click_on_logo(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.account_button)).click()
        driver.find_element(By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']").click()
        a = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.make_burger_header))
        assert a

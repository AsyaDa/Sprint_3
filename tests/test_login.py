from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locators


class TestLogin:
    def test_login_by_enter_button(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_login_by_personal_account_button(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.account_button)).click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_login_by_link_on_forgot_password_page(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.account_button)).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='Восстановить пароль']"))).click()
        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_login_by_link_on_registration_page(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.account_button)).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='Зарегистрироваться']"))).click()
        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_login(self, login):
        driver = login
        a = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.place_order_button))
        assert a


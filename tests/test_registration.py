from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locator import Locators
faker = Faker()


class TestRegistration:
    def test_registration_with_incorrect_password(self, driver):
        email = faker.email()
        name = faker.name()
        password = "12345"
        print(email)
        print(name)
        driver.find_element(*Locators.account_button).click() #кликаем на кнопку Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.go_to_registration_page_button)).click() #ждем и кликаем на кнопку Зарегистрироваться
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Регистрация']"))) #ждем, чтобы убедиться, что мы на странице регистрации
        driver.find_element(*Locators.name_form).send_keys(name) #вводим тестовое имя пользователя
        driver.find_element(*Locators.email_form).send_keys(email) #вводим тестовый email пользователя
        driver.find_element(*Locators.password_form).send_keys(password) #вводим тестовый пароль пользователя
        driver.find_element(*Locators.registration_button).click() #кликаем на кнопку Зарегистрироваться
        a = driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']").text
        assert a == "Некорректный пароль"

    def test_registration(self, driver):
        email = faker.email()
        name = faker.name()
        password = "123456"
        print(email)
        print(name)
        driver.find_element(*Locators.account_button).click()  # кликаем на кнопку Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.go_to_registration_page_button)).click() #ждем и кликаем на кнопку Зарегистрироваться
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Регистрация']"))) #ждем, чтобы убедиться, что мы на странице регистрации
        driver.find_element(*Locators.name_form).send_keys(name)  # вводим тестовое имя пользователя
        driver.find_element(*Locators.email_form).send_keys(email)  # вводим тестовый email пользователя
        driver.find_element(*Locators.password_form).send_keys(password)  # вводим тестовый пароль пользователя
        driver.find_element(*Locators.registration_button).click()  # кликаем на кнопку Зарегистрироваться
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.login_button_on_entry_page))
        driver.find_element(*Locators.email_form).send_keys(email)  # вводим тестовый email пользователя
        driver.find_element(*Locators.password_form).send_keys(password)  # вводим тестовый пароль пользователя
        driver.find_element(*Locators.login_button_on_entry_page).click()  # кликаем на кнопку Войти
        a = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.place_order_button))
        assert a

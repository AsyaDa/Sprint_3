from selenium.webdriver.common.by import By


class Locators:
    account_button = (By.XPATH, ".//p[text()='Личный Кабинет']") #кнопка перехода в личный кабинет
    go_to_registration_page_button = (By.XPATH, ".//a[@href='/register']") #кнопка перехода на страницу регистрации пользователя
    name_form = (By.XPATH, "//label[text()='Имя']/following-sibling::input") #кнопка для ввода имени пользователя
    email_form = (By.XPATH, "//label[text()='Email']/following-sibling::input") #форма для ввода почты
    password_form = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") #форма для ввода пароля
    registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка зарегистрироваться
    current_section = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]") #активный раздел конструктора
    place_order_button = (By.XPATH, ".//button[text()='Оформить заказ']") #кнопка оформления заказа
    login_button_on_entry_page = (By.XPATH, ".//button[text()='Войти']") #кнопка Войти на странице входа
    make_burger_header = (By.XPATH, ".//h1[text()='Соберите бургер']") #заголовок Соберите бургер
from selenium.webdriver.common.by import By
class TestLocators:
    SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(@class, 'button_button_size_large')]") # кнопка "Войти в аккаунт"
    REGISTER_BUTTON_ON_ENTER_PAGE = (By.LINK_TEXT, 'Зарегистрироваться') # Кнопка "Зарегистрироваться" на странице входа
    NAME_INPUT_ON_REG_PAGE = (By.XPATH, '//input[@name="name"]') # поле ввода Имени при регистрации
    EMAIL_INPUT_ON_REG_PAGE = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # поле ввода Email при регистрации
    PASSWORD_INPUT_ON_REG_PAGE = (By.XPATH, '//input[@name="Пароль"]') # поле ввода пароля при регистрации
    REGISTER_BUTTON_ON_REG_PAGE = (By.XPATH, "//*[contains(text(),'Зарегистрироваться')]") # кнопка зарегистрироваться
    HEADER_ON_ENTER_PAGE = (By.XPATH, "//h2[text()='Вход']") # закголовок страницы входа
    TEXT_INVALID_PASSWORD_ON_REG_PAGE = (By.XPATH, '//p[@class = "input__error text_type_main-default"]') # неверный ввод пароля при регистрации
    HEADER_ON_REG_PAGE = (By.XPATH, '//h2[text()="Регистрация"]') # заголовок страницы регистрации
    EMAIL_INPUT_ON_ENTER_PAGE = (By.XPATH, '//input[@name = "name"]') # поле ввода email при входе
    PASSWORD_INPUT_ON_ENTER_PAGE = (By.XPATH, '//input[@name = "Пароль"]') # поля пароля на странице входа
    ENTER_BUTTON_ON_PAGE_ENTER = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка входа после заполнения полей
    HEADER_ON_MAIN_PAGE = (By.XPATH, "//h1[text()='Соберите бургер']") # заголовок главной страницы после прохождения аутентификации
    BUTTON_MY_ACCOUNT = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]') # Кнопка "Личный кабинет" на главной странице
    BUTTON_ENTER_ON_REG_PAGE = (By.XPATH, '//a[text()="Войти"]') # кнопка Войти на старнице Регистрации
    BUTTON_RECOVERY_PASS = (By.LINK_TEXT, 'Восстановить пароль') # Кнопка восстановления пароля
    BUTTON_ENTER_ON_RECOVERY_PAGE = (By.LINK_TEXT, 'Войти') #Кнопка войти на странице восстановления пароля
    BUTTON_LOGOUT = (By.XPATH, '//button[contains(text(),"Выход")]') #кнопка выхода из аккаунта
    PAGE_MY_ACCOUNT = (By.XPATH, '//a[text()="Профиль"]') # Страница личного кабинета
    TAB_SAUCES = (By.XPATH, '//span[contains(text(),"Соусы")]') # вкладка Соусы
    HEADER_TAB_SAUCES = (By.XPATH, '//h2[contains(text(),"Соусы")]') # заголовок вкладки Соусы
    TAB_TOPPING = (By.XPATH, '//span[contains(text(),"Начинки")]') # вкладка Начинки
    HEADER_TAB_TOPPING = (By.XPATH, '//span[contains(text(),"Начинки")]') # заголовок вкладки Начинки
    TAB_BUNS = By.XPATH, '//span[contains(text(),"Булки")]' # вкладка Булки
    HEADER_TAB_BUNS = (By.XPATH, '//span[contains(text(),"Булки")]')# заголовек вкладки Булки
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]") # Кнопка "Конструктор" в Хедере страницы
    BUTTON_LOGO = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]') # Логотип в хедере страницы

from selenium.webdriver.common.by import By

class StartPageLocators:

    ENTER_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    CREATE_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")
    BUN_N200i = (By.XPATH, ".//p[text()='Краторная булка N-200i']")
    ORDER_DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    CLOSE_ORDER_DETAILS = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    DRUG_AND_DROP_BUN = (By.XPATH, './/*[text()="Перетяните булочку сюда (низ)"]')
    ORDER_COUNT = (By.XPATH, ".//*[@class ='counter_counter__num__3nue1'and text()='2']")
    CONFIRM_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_IS_CREATING = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")

class RecoveryPasswordLocators:

    BUTTON_RECOVERY = (By.XPATH, ".//button[text()='Восстановить']")
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, ".//div[@class='input__icon input__icon-action']")
    ACTIVE_PASSWORD = (By.CSS_SELECTOR, '.input.input_status_active')
    RESET_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")
    RECOVERY_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")

class PersonalAccountLocators:

    PROFILE_BUTTON = (By.XPATH, ".//a[text()='Профиль']")
    HISTORY_BUTTON = (By.XPATH, ".//a[text()='История заказов']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    LAST_ORDER_NUMBER = (By.XPATH, './/li[last()]/a[contains(@href, "order-history")]/*/p[1]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    NAME_FIELD = (By.XPATH, ".//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")
    LOG_IN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

class OrderFeedLocators:
    FIRST_ORDER = (By.XPATH, './/*[contains(@class, "OrderHistory_link")]')
    COMPOUND_ORDER = (By.XPATH, ".//p[text()='Cостав']")
    ORDER_NUMBERS = (By.XPATH, './/ul[contains(@class,"OrderFeed_list")]//p[contains(text(),"#")]')
    ORDERS_COUNTER_ALL_TIME = (By.XPATH, './/p[text()="Выполнено за все время:"]/following-sibling::''p[contains(@class,"OrderFeed_number")]')
    ORDERS_COUNTER_TODAY = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"OrderFeed_number")]')
    ORDER_NUMBER = (By.XPATH, ".//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text ""text_type_digits-large mb-8']")
    ORDER_NUMBER_IN_WORK = (By.XPATH, ".//ul[contains(@class, 'ListReady')]/li")
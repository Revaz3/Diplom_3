from pages.personal_account_page import PersonalAccountPage
from data import Buttons, Urls
import allure
from pages.start_page import StartPage
from conftest import driver

@allure.suite('Тестируем личный кабинет')
class TestPersonalAccountPage:

    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    def test_transition_personal_account_button(self, driver):
        start_page = StartPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        personal_account_page.click_personal_account()
        assert personal_account_page.find_profile_button().text == Buttons.PROFILE_BUTTON_TEXT

    @allure.title('Проверяем переход в раздел «История заказов»')
    def test_history_order(self, driver):
        start_page = StartPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        personal_account_page.click_personal_account()
        personal_account_page.click_history_order_button()
        assert personal_account_page.get_current_url() == f"{Urls.MAIN_PAGE}{Urls.ORDER_HISTORY_PAGE}"

    @allure.title('Проверяем выход из аккаунта')
    def test_log_out_account(self, driver):
        start_page = StartPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        personal_account_page.click_personal_account()
        personal_account_page.click_exit_button()
        assert personal_account_page.find_enter_button().text == Buttons.ENTER_BUTTON_TEXT
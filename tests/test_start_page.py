from pages.personal_account_page import PersonalAccountPage
from pages.start_page import StartPage
from data import Urls, Buttons
import allure
from conftest import driver

@allure.suite('Тестируем основной функционал')
class TestMainPage:

    @allure.title('Проверяем переход по клику на «Конструктор»')
    def test_transition_constructor(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        start_page = StartPage(driver)
        start_page.click_order_feed_button()
        personal_account_page.wait_for_personal_account_button()
        start_page.click_constructor_button()
        assert start_page.find_create_order().is_displayed

    @allure.title('Проверяем переход по клику на «Лента заказов»')
    def test_transition_order_feed(self, driver):
        start_page = StartPage(driver)
        start_page.click_order_feed_button()
        assert start_page.get_current_url() == f"{Urls.MAIN_PAGE}{Urls.ORDER_FEED_PAGE}"

    @allure.title('Проверяем, если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, driver):
        start_page = StartPage(driver)
        start_page.click_ingredient_button()
        assert start_page.find_order_details().text == Buttons.ORDER_DETAILS

    @allure.title('Проверяем, что всплывающее окно закрывается кликом по крестику,')
    def test_close_order_details(self, driver):
        start_page = StartPage(driver)
        start_page.click_ingredient_button()
        start_page.close_ingredient_details()
        assert start_page.find_create_order().is_displayed

    @allure.title('Проверяем, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_in_order(self, driver):
        start_page = StartPage(driver)
        start_page.add_ingredient()
        assert start_page.check_order_count() == '2'

    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ')
    def test_make_order_autorized_account(self, driver):
        start_page = StartPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        start_page.add_ingredient()
        start_page.click_confirm_order()
        assert start_page.order_is_creating().text == Buttons.ORDER_IS_CREATING
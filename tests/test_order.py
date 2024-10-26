from pages.order_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from pages.start_page import StartPage
from data import Buttons
import allure
from conftest import driver

@allure.suite('Тестируем раздел «Лента заказов»')
class TestOrderFeed:

    @allure.title('Проверяем, если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details_info(self, driver):
        order_feed_page = OrderFeedPage(driver)
        start_page = StartPage(driver)
        start_page.click_order_feed_button()
        order_feed_page.click_first_order()
        assert order_feed_page.find_compound_text().text == Buttons.COMPOUND_TEXT

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_find_order_in_feed(self, driver):
        order_feed_page = OrderFeedPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        start_page = StartPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        start_page.make_order()
        personal_account_page.click_personal_account()
        personal_account_page.click_history_order_button()
        order_number = personal_account_page.get_last_order_number()
        start_page.click_history_button()
        assert order_number in order_feed_page.get_order_numbers()

    @allure.title('Проверяем, что при создании нового заказа счётчик «Выполнено за всё время увеличивается»')
    def test_all_time_order_counter(self, driver):
        order_feed_page = OrderFeedPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        start_page = StartPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        start_page.click_history_button()
        counter_order = order_feed_page.get_all_time_numbers_of_orders()
        start_page.click_constructor_button()
        start_page.make_order()
        start_page.click_history_button_with_wait()
        new_counter_order = order_feed_page.get_all_time_numbers_of_orders()
        assert new_counter_order > counter_order

    @allure.title('Проверяем, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_today_order_counter(self, driver):
        order_feed_page = OrderFeedPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        start_page = StartPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        start_page.click_history_button()
        counter_order = order_feed_page.get_today_numbers_of_orders()
        start_page.click_constructor_button()
        start_page.make_order()
        start_page.click_history_button_with_wait()
        new_counter_order = order_feed_page.get_today_numbers_of_orders()
        assert new_counter_order > counter_order

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе «В работе»')
    def test_order_in_work(self, driver):
        order_feed_page = OrderFeedPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        start_page = StartPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        start_page.add_ingredient()
        start_page.click_confirm_order()
        order_number = order_feed_page.get_order_number_with_template()
        start_page.close_ingredient_details()
        start_page.click_history_button_with_wait()
        order_number_in_work = order_feed_page.get_order_numer_in_work_with_template()
        assert f"0{order_number}" == order_number_in_work
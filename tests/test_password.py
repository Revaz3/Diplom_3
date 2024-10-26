from pages.password_page import RecoveryPasswordPage
from data import Urls
import allure
from pages.start_page import StartPage
from conftest import driver

@allure.suite('Тестируем восстановление пароля')
class TestRecoveryPassword:

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_transition_recovery_page(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        start_page = StartPage(driver)
        start_page.click_enter_personal_account()
        recovery_password_page.click_recovery_button()
        assert recovery_password_page.get_current_url() == f"{Urls.MAIN_PAGE}{Urls.RECOVERY_PAGE}"

    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_button(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        start_page = StartPage(driver)
        start_page.click_enter_personal_account()
        recovery_password_page.click_recovery_button()
        recovery_password_page.set_text_email_field()
        recovery_password_page.click_button_recovery()
        recovery_password_page.wait_for_save_button()
        assert recovery_password_page.get_current_url() == f"{Urls.MAIN_PAGE}{Urls.RESET_PAGE}"

    @allure.title('Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_visibility_password(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        start_page = StartPage(driver)
        start_page.click_enter_personal_account()
        recovery_password_page.click_recovery_button()
        recovery_password_page.set_text_email_field()
        recovery_password_page.click_button_recovery()
        recovery_password_page.wait_for_save_button()
        recovery_password_page.set_password()
        recovery_password_page.click_show_password()
        assert recovery_password_page.check_password()
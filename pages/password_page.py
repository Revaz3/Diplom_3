from pages.base_page import BasePage
from locators import RecoveryPasswordLocators
from data import TestData
import allure

class RecoveryPasswordPage(BasePage):

    @allure.step('Кликаем с ожиданием на кнопку «Восстановить пароль»')
    def click_recovery_button(self):
        self.click_element_with_wait(RecoveryPasswordLocators.RECOVERY_BUTTON)

    @allure.step('Вводим почту')
    def set_text_email_field(self):
        self.set_text(RecoveryPasswordLocators.EMAIL_FIELD, TestData.test_email)

    @allure.step('Кликаем с ожиданием на кнопку «Восстановить»')
    def click_button_recovery(self):
        self.click_element_with_wait(RecoveryPasswordLocators.BUTTON_RECOVERY)

    @allure.step('Кликаем с ожиданием на кнопку «Сохранить»')
    def wait_for_save_button(self):
        self.find_element_with_wait(RecoveryPasswordLocators.RESET_BUTTON)

    @allure.step('Вводим пароль')
    def set_password(self):
        self.set_text(RecoveryPasswordLocators.PASSWORD_FIELD, TestData.test_password)

    @allure.step('Кликаем на иконку «Показать пароль»')
    def click_show_password(self):
        self.click_element(RecoveryPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверяем пароль')
    def check_password(self):
        return self.wait_for_visibility_element(RecoveryPasswordLocators.ACTIVE_PASSWORD)
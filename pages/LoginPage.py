from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    GET_QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RESTORE_ACCESS_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@data-l="t,register" and contains(@tsid, "login-block")]')
    LOGIN_VIA_VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_VIA_MAILRU_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_VIA_YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    GO_BACK_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login-help portlet_f"]')
    PROFILE_RECOVERY_BUTTON = (By.XPATH, '//*[@name="st.go_to_recovery"]')

class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.GET_QR_BUTTON)
        self.find_element(LoginPageLocators.RESTORE_ACCESS_LINK)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_VIA_VK_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_VIA_MAILRU_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_VIA_YANDEX_BUTTON)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step("Заполняем поле 'Логин")
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step("Заполняем поле 'Пароль")
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step("Переходим к восстановлению")
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.PROFILE_RECOVERY_BUTTON).click()

    @allure.step("Переходим к регистрации")
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTER_BUTTON).click()

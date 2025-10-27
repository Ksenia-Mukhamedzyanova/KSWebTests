from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

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

class LoginPageHelper(BasePage):
    pass

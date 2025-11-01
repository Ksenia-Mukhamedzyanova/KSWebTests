from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisemenuCabinetHelp import AdvertisementCabinetHelpHelper
import allure

BASE_URL = 'https://ok.ru/help'

@allure.suite("Проверка страницы поддержки")
@allure.title("Проверка возможности перехода на страницу 'Рекламный кабинет'")
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scroll_to_item(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_contacts_page(self):
        link = self.browser.find_element(*MainPageLocators.CONTACS)
        link.click()

'''Модуль содержащий реализацию Page Object Model для главной страницы.'''

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    '''Класс содержащий методы для главной страницы'''
    def go_to_contacts_page(self):
        '''Метод перехода на страницу контакты'''
        link = self.browser.find_element(*MainPageLocators.CONTACS)
        link.click()

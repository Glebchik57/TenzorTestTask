'''Модуль содержащий реализацию Page Object Model для страницы tensor.'''

from .base_page import BasePage
from .locators import TensorPageLocators


class TensorPage(BasePage):
    '''Класс содержащий методы страницы tensor'''
    def should_be_power_in_people_block(self):
        '''Метод проверки наличия блока сила в людях'''
        assert self.is_element_present(*TensorPageLocators.POWER_IN_PEOPLE), 'Блок "Сила в людях" отсутствует'

    def go_to_about(self):
        '''Метод перехода на страницу about'''
        link = self.browser.find_element(*TensorPageLocators.MORE)
        super().scrol_to_el(link)
        link.click()

'''Модуль содержащий реализацию базового класса для Page Object Model.'''

from selenium.common.exceptions import NoSuchElementException


class BasePage():
    '''Класс содержащий инициализацию и базовые методы для POM'''

    def __init__(self, browser, url, timeout=10):
        '''Инициализация'''
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        '''Метод перехода по URL'''
        self.browser.get(self.url)

    def change_window(self):
        '''Метод переключения между вкладками'''
        new_page = self.browser.window_handles[1]
        self.browser.switch_to.window(new_page)

    def scrol_to_el(self, element):
        '''Метод скролинга до элемента'''
        self.browser.execute_script(
            "return arguments[0].scrollIntoView(true);",
            element
        )

    def is_element_present(self, how, what):
        '''Метод проверки существования элемента'''
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

'''Модуль содержащий тесты'''

from pages.locators import MainPageLocators, TensorPageLocators, AboutPageLocators, ContacsPageLocators
from pages.main_page import MainPage
from pages.contact_page import ContactsPage
from pages.tensor_page import TensorPage
from pages.about_page import AboutPage

import time


class TestCase1():
    '''Класс содержащий тесты для сценария №1'''
    def test_shoukd_be_power_in_pepople(self, browser):
        '''Метод проверяющий наличия блока сила в людях'''
        page = MainPage(
            browser,
            MainPageLocators.SELF_LINK
        )
        page.open()
        page.go_to_contacts_page()
        contact_page = ContactsPage(browser, browser.current_url)
        contact_page.go_to_tensor()
        contact_page.change_window()
        tensor_page = TensorPage(browser, browser.current_url)
        tensor_page.should_be_power_in_people_block()

    def test_about_should_be_right(self, browser):
        '''Метод проверяющий верность URL страницы about'''
        page = TensorPage(browser, TensorPageLocators.SELF_LINK)
        page.open()
        page.go_to_about()
        about_page = AboutPage(browser, browser.current_url)
        about_page.url_about_is_right()

    def test_pictures_should_be_same_size(self, browser):
        '''Метод проверки соответствия размеров картинок друг другу'''
        page = AboutPage(browser, AboutPageLocators.SELF_LINK)
        page.open()
        page.pictures_have_same_sizes()


class TestCase2():
    '''Класс содержащий тесты для сценария №2'''
    def test_should_be_right_region_partners_there_are(self, browser):
        '''Метод проверки правильности выбора региона и наличия блока партнеры'''
        page = MainPage(
            browser,
            MainPageLocators.SELF_LINK
        )
        page.open()
        page.go_to_contacts_page()
        contact_page = ContactsPage(browser, browser.current_url)
        contact_page.region_is_right_partners_there_are()

    def test_change_region(self, browser):
        '''Метод проверки смены региона'''
        contact_page = ContactsPage(browser, ContacsPageLocators.SELF_LINK)
        contact_page.open()
        old_inf = contact_page.get_information_current_region()
        contact_page.change_region()
        time.sleep(10)
        new_inf = contact_page.get_information_current_region()
        contact_page.check_region_was_changed(old_inf, new_inf)

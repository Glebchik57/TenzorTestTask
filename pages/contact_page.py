from .base_page import BasePage
from .locators import ContacsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class ContactsPage(BasePage):
    def go_to_tensor(self):
        link = self.browser.find_element(*ContacsPageLocators.BANER)
        link.click()

    def region_is_right_partners_there_are(self):
        region = self.browser.find_element(*ContacsPageLocators.REGION)
        assert region.text == 'Калининградская обл.', 'Регион определился неверно'
        assert self.is_element_present(*ContacsPageLocators.PARTNERS), 'Блок "Партнеры" отсутствует'

    def get_information_current_region(self):
        region_inf = []
        name = self.browser.find_element(*ContacsPageLocators.REGION)
        url = self.browser.current_url
        title = self.browser.title
        information_partners_block = []
        for i in self.browser.find_elements(*ContacsPageLocators.PARTNERSNAMES):
            information_partners_block.append(i.text)
        region_inf.append(name.text)
        region_inf.append(url)
        region_inf.append(title)
        region_inf.append(information_partners_block)
        return region_inf

    def change_region(self):
        wait = WebDriverWait(self.browser, 20)
        region = self.browser.find_element(*ContacsPageLocators.REGION)
        region.click()
        time.sleep(10)
        # target_region = self.browser.find_element(*ContacsPageLocators.KAMCHATKA)
        wait.until(EC.element_to_be_clickable(ContacsPageLocators.KAMCHATKA)).click()
        #time.sleep(10)
        # target_region.click()
        #wait.until(EC.text_to_be_present_in_element(ContacsPageLocators.REGION, 'Камчатский край'))

    def check_region_was_changed(self, old_inf, new_inf):
        for i in range(len(old_inf)):
            if i == 0:
                assert old_inf[i] != new_inf[i], 'Регион возле заголовка "контакты" не поменялся'
            elif i == 1:
                assert old_inf[i] != new_inf[i], 'URL страницы не изменился'
            elif i == 2:
                assert old_inf[i] != new_inf[i], 'title вкладки не поменялся'
            elif i == 3:
                assert old_inf[i] != new_inf[i], 'Список партнеров не поменялся'

        # assert old_inf != new_inf, 'Информация на странице не поменялась'

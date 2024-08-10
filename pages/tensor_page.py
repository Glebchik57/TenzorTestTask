from .base_page import BasePage
from .locators import TensorPageLocators


class TensorPage(BasePage):
    def should_be_power_in_people_block(self):
        assert self.is_element_present(*TensorPageLocators.POWER_IN_PEOPLE), 'Блок "Сила в людях" отсутствует'

    def go_to_about(self):
        link = self.browser.find_element(*TensorPageLocators.MORE)
        super().scrol_to_el(link)
        link.click()

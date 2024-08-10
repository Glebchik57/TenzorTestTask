from .base_page import BasePage
from .locators import AboutPageLocators


class AboutPage(BasePage):
    def url_about_is_right(self):
        url = 'https://tensor.ru/about'
        assert self.browser.current_url == url, 'URL не соответсвует необходимому'

    def pictures_have_same_sizes(self):
        flag_img = True
        images = self.browser.find_elements(*AboutPageLocators.PHOTOS)
        info = []
        for image in images:
            width = image.get_attribute("width")
            height = image.get_attribute("height")
            info.append((width, height))
        w = info[0][0]
        h = info[0][1]
        for i in info[1:]:
            if i[0] == w and i[1] == h:
                continue
            else:
                flag_img = False
        assert flag_img, 'Фотографии в блоке "Работаем" разного размера'

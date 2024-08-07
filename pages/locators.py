from selenium.webdriver.common.by import By

class BasePageLocators():
    CONTACS = (By.LINK_TEXT, 'Контакты')


class ContacsPageLocators():
    BANER = (By.XPATH, "//a[@title='tensor.ru']")
    REGION = (By.CSS_SELECTOR, 'sbis_ru-Region-Chooser__text')  #уточнить
    PARTNERS = (By.CSS_SELECTOR, '???')
    KAMCHATKA = (By.CSS_SELECTOR, '???')
    LOCAL_VER = (By.CSS_SELECTOR, '???')


class TensorPageLocators():
    POWER_IN_PEOPLE = (By.CSS_SELECTOR, 'tensor_ru-Index__block4-content tensor_ru-Index__card')
    MORE = (By.CSS_SELECTOR, '???')


class AboutPageLocators():
    WORKING = (By.CSS_SELECTOR, '???')
    PHOTOS = (By.CSS_SELECTOR, '???')


class DownloadPageLocators():
    WEB_DOWNLOADER = (By.CSS_SELECTOR, '???')

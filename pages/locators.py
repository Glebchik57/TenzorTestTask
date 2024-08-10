from selenium.webdriver.common.by import By


class MainPageLocators():
    SELF_LINK = 'https://sbis.ru/'
    CONTACS = (By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')


class ContacsPageLocators():
    SELF_LINK = 'https://sbis.ru/contacts/'
    BANER = (By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor.mb-12')
    REGION = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser.ml-16.ml-xm-0 .sbis_ru-link')
    PARTNERS = (By.CSS_SELECTOR, '[name="itemsContainer"]')
    PARTNERSNAMES = (By.CSS_SELECTOR, '.sbisru-Contacts-List__name')
    KAMCHATKA = (By.CSS_SELECTOR, '[title="Камчатский край"]')
    KAMCHATKA_FLAG = (By.XPATH, "//span[@title='Камчатский край']")


class TensorPageLocators():
    SELF_LINK = 'https://tensor.ru/'
    POWER_IN_PEOPLE = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    MORE = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card .tensor_ru-link')


class AboutPageLocators():
    SELF_LINK = 'https://tensor.ru/about'
    WORKING = (By.CSS_SELECTOR, '.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')
    PHOTOS = (By.CSS_SELECTOR, '.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 img')


class DownloadPageLocators():
    WEB_DOWNLOADER = (By.CSS_SELECTOR, '???')

from selenium.common.exceptions import NoSuchElementException


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def change_window(self):
        new_page = self.browser.window_handles[1]
        self.browser.switch_to.window(new_page)

    def scrol_to_el(self, element):
        self.browser.execute_script(
            "return arguments[0].scrollIntoView(true);",
            element
        )

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

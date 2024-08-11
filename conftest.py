'''Модуль фикстур'''

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    '''Фикстура доступа к вебдрайверу'''
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

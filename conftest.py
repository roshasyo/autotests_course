import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Language for the browser interface')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    
    # Запуск браузера
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield browser
    browser.quit()

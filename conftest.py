import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\nStart browser with language={language}")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nQuit browser")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')
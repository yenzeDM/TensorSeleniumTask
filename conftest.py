from time import sleep
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome import service
from webdriver_manager.opera import OperaDriverManager
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: --browser_name=Your browser")


@pytest.fixture(scope='function')
def driver(request):
    """Return a suitable browser for test"""
    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        options = ChromeOptions()
        servise = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=servise, options=options)
    elif browser_name == 'edge':
        options = EdgeOptions()
        servise = EdgeService(EdgeChromiumDriverManager().install())
        browser = webdriver.Edge(service=servise, options=options)
    elif browser_name == 'opera':
        options = ChromeOptions()
        options.add_experimental_option('w3c', True)
        opera_servise = service.Service(OperaDriverManager().install())
        opera_servise.start()
        browser = webdriver.Remote(opera_servise.service_url, options=options)
    else:
        raise pytest.UsageError('You are choosing an unavailable browser')
    yield browser
    print("\nquit browser..")
    sleep(3)
    browser.quit()

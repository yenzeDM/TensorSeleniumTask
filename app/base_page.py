from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open_website(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def is_element_present(self, method, css_celector):
        try:
            self.driver.find_element(method, css_celector)
        except NoSuchElementException as ex:
            print(ex)
            return False
        return True
    
    def is_elements_present(self, method, css_celector):
        try:
            self.driver.find_elements(method, css_celector)
        except NoSuchElementException as ex:
            print(ex)
            return False
        return True
    
    def check_url(self, url):
        current_url = self.driver.current_url
        print(current_url)
        assert current_url == url, 'Your url address is different'

    def check_window_name(self, name):
        browser_window = self.driver.title
        assert name in browser_window, 'Your title inside browser window is different'
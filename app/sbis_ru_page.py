from .base_page import BasePage
from .locators import SbisRuPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SbisRuPage(BasePage):
        
    def go_to_contact_page(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(SbisRuPageLocators.GO_TO_CONTACT_PAGE)).click()

    def go_to_download_page(self):
        download = self.driver.find_element(*SbisRuPageLocators.GO_TO_DOWNLOAD_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", download)
        download.click()
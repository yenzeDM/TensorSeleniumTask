import pytest
from .base_page import BasePage
from .locators import SbisRuDownloadPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import wget
import os
import re


def round_float(float_number, amount):
    float_number = str(float_number)
    after_dot = float_number[float_number.find('.') + 1:]
    before_dot = float_number[:float_number.find('.') + 1]
    if after_dot[:amount + 1][-1] in ['0', '1', '2', '3', '4']:
        return float(before_dot + after_dot[:amount])
    elif after_dot[:amount + 1][-1] in ['5', '6', '7', '8', '9']:
        result = str(int(after_dot[:amount][-1]) + 1)
        return float(before_dot + after_dot[:amount - 1] + result)

class SbisRuDownloadPage(BasePage):

    def select_vlsi_plagin(self):
        vlsi_plagin = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(SbisRuDownloadPageLocators.SELECT_VLSI_PLAGIN))               #self.driver.find_element(*SbisRuDownloadPageLocators.SELECT_VLSI_PLAGIN)
        self.driver.execute_script('arguments[0].click()', vlsi_plagin)

    def select_windows_os(self):
        windows_os = self.driver.find_element(*SbisRuDownloadPageLocators.SELECT_WINDOWS_OS)
        self.driver.execute_script('arguments[0].click()', windows_os)

    def download_web_installer(self):
        url = 'https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe'
        file_name = wget.download(url, out='download/third_script')
        try:
            os.path.isfile(file_name)
        except Exception as ex:
            print(ex)
            pytest.UsageError('The file did not download')

    def check_file_size(self):
        current_file_size = os.path.getsize('download\\third_script\\sbisplugin-setup-web.exe')

        file_size_on_the_page = self.driver.find_element(*SbisRuDownloadPageLocators.CHECK_FILE_SIZE).text
        pattern = r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?'
        file_size_on_the_page = re.search(pattern, file_size_on_the_page).group(0)

        current_file_size = round_float(float((current_file_size / 1024) / 1024), 2)
        file_size_on_the_page = round(float(file_size_on_the_page), 2)

        assert current_file_size == file_size_on_the_page, 'The sizes on the downloaded file and on the web page are different'

        

        
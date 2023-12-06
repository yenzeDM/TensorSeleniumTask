import pytest
from .app.sbis_ru_page import SbisRuPage
from .app.sbis_ru_download_page import SbisRuDownloadPage


@pytest.mark.third_script
class TestThirdSrcipt:

    def test_user_can_go_to_download_page(self, driver):
        url = 'https://sbis.ru/'
        page = SbisRuPage(driver, url)
        page.open_website()
        page.go_to_download_page()

    def test_user_can_select_vlsi_plagin(self, driver):
        url = 'https://sbis.ru/download?tab=ereport&innerTab=ereport25'
        page = SbisRuDownloadPage(driver, url)
        page.open_website()
        page.select_vlsi_plagin()

    def test_user_can_select_windows_os(self, driver):
        url = 'https://sbis.ru/download?tab=plugin&innerTab=linux'
        page = SbisRuDownloadPage(driver, url)
        page.open_website()
        page.select_windows_os()

    def test_user_can_download_web_installer(self, driver):
        url = 'https://sbis.ru/download?tab=plugin&innerTab=default'
        page = SbisRuDownloadPage(driver, url)
        page.open_website()
        page.download_web_installer()

    def test_check_file_size(self, driver):
        url = 'https://sbis.ru/download?tab=plugin&innerTab=default'
        page = SbisRuDownloadPage(driver, url)
        page.open_website()
        page.check_file_size()
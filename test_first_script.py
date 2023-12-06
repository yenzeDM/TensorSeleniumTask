import pytest
from .app.sbis_ru_page import SbisRuPage
from .app.contacts_page import ContactPage
from .app.tensor_ru_page import TensorRuPage
from .app.tensor_about_page import TensorAboutPage


@pytest.mark.first_script
class TestFirstScript:

    def test_user_can_go_to_contact_page(self, driver):
        url = 'https://sbis.ru/'
        page = SbisRuPage(driver, url)
        page.open_website()
        page.go_to_contact_page()

    def test_user_can_click_on_tensor_banner(self, driver):
        url = 'https://sbis.ru/contacts/33-vladimirskaya-oblast?tab=clients'
        page = ContactPage(driver, url)
        page.open_website()
        page.click_on_tensor_banner()

    def test_user_can_see_block_power_is_in_people(self, driver):
        url = 'https://tensor.ru/'
        page = TensorRuPage(driver, url)
        page.open_website()
        page.is_block_power_is_in_people()

    def test_user_can_click_more_details_into_block_power_is_in_people(self, driver):
        url = 'https://tensor.ru/'
        page = TensorRuPage(driver, url)
        page.open_website()
        page.click_on_more_details_into_block_power_is_in_people()

    def test_pictures_have_the_same_height_and_width(self, driver):
        url = 'https://tensor.ru/about'
        page = TensorAboutPage(driver, url)
        page.open_website()
        page.pictures_have_the_same_height_and_width()

import pytest
from .app.sbis_ru_page import SbisRuPage
from .app.contacts_page import ContactPage


@pytest.mark.second_script
class TestSecondScript:

    def test_user_can_go_to_contact_page(self, driver):
        url = 'https://sbis.ru/'
        page = SbisRuPage(driver, url)
        page.open_website()
        page.go_to_contact_page()

    def test_user_can_see_correct_region(self, driver):
        url = 'https://sbis.ru/contacts/33-vladimirskaya-oblast?tab=clients'
        page = ContactPage(driver, url)
        page.open_website()
        page.correct_region_selected('Владимирская обл.')

    def test_user_can_see_partners_list_of_vladimir_region(self, driver):
        url = 'https://sbis.ru/contacts/33-vladimirskaya-oblast?tab=clients'
        page = ContactPage(driver, url)
        page.open_website()
        page.is_list_partners_of_vladimir_region()

    def test_user_can_change_region(self, driver):
        url = 'https://sbis.ru/contacts/33-vladimirskaya-oblast?tab=clients'
        page = ContactPage(driver, url)
        page.open_website()
        page.change_region()

    def test_user_can_see_partners_list_of_kamchatka_krai(self, driver):
        url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
        page = ContactPage(driver, url)
        page.open_website()
        page.is_list_partners_of_kamchatka_krai()

    def test_user_can_see_correct_region_after_changed(self, driver):
        url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
        page = ContactPage(driver, url)
        page.open_website()
        page.correct_region_selected('Камчатский край')

    def test_user_can_see_correct_url(self, driver):
        url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
        page = ContactPage(driver, url)
        page.open_website()
        page.check_url(url)

    def test_user_can_see_correct_tittle_inside_window(self, driver):
        url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
        page = ContactPage(driver, url)
        page.open_website()
        page.check_window_name('Камчатский край')
        
from .base_page import BasePage
from .locators import ContactPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ContactPage(BasePage):
    CORRECT_PARTNERS_OF_VLADIMIR_REGION = ['СБИС - Владимир', 'ООО "ИнфоЦентр"', 'ИП Малинин Юрий Геннадьевич', 'ИП Гаев Н.А.', 'Радар Сервис', 'НаВигатор+',
                                           'Центр Оперативного Сервиса', 'Техцентр', 'ЭЛО', 'ИП Бондарь Ю.В.', 'Альфа', 'Цифра, ООО', 'ООО"Радар Сервис"', 'ИП Курдюков И.А.', 'ИП Щелканова Полина Александровна']
    CORRECT_PARTNERS_OF_KAMCHATKA_KRAI = ['СБИС - Камчатка']

    def click_on_tensor_banner(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
            ContactPageLocators.CLICK_ON_TENSOR_BANNER)).click()

    def correct_region_selected(self, correct_region):
        region = self.is_element_present(
            *ContactPageLocators.CORRECT_REGION_SELECTED)
        region = self.driver.find_element(
            *ContactPageLocators.CORRECT_REGION_SELECTED).text
        assert region == correct_region, 'Your region is not correct'

    def is_list_partners_of_vladimir_region(self):
        current_partners_on_the_page = [
            i.text for i in self.driver.find_elements(*ContactPageLocators.PARTNERS)]
        assert self.CORRECT_PARTNERS_OF_VLADIMIR_REGION == current_partners_on_the_page, 'Current partners on the page are not correct'
        current_partners_on_the_page.clear()

    def is_list_partners_of_kamchatka_krai(self):
        current_partners_on_the_page = self.driver.find_element(
            *ContactPageLocators.PARTNERS).text
        assert self.CORRECT_PARTNERS_OF_KAMCHATKA_KRAI[
            0] == current_partners_on_the_page, 'Current partners on the page are not correct'

    def change_region(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
            ContactPageLocators.CORRECT_REGION_SELECTED)).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
            ContactPageLocators.CHANGE_REGION)).click()

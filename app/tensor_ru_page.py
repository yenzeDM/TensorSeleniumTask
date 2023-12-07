from .base_page import BasePage
from .locators import TensorRuPageLocators


class TensorRuPage(BasePage):

    def is_block_power_is_in_people(self):
        self.is_element_present(
            *TensorRuPageLocators.IS_BLOCK_POWER_IS_IN_PEOPLE)
        title = self.driver.find_element(*TensorRuPageLocators.TITLE).text
        assert title == 'Сила в людях', 'You have a wrong title should be "Сила в людях"'

    def click_on_more_details_into_block_power_is_in_people(self):
        more_details = self.driver.find_element(
            *TensorRuPageLocators.CLICK_MORE_DETAILS_IN_BLOCK_POWER_IS_IN_PEOPLE)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", more_details)
        more_details.click()

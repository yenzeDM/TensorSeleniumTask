from .base_page import BasePage
from .locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):

    def pictures_have_the_same_height_and_width(self):
        all_height = []
        all_width = []

        picture = self.driver.find_element(
            *TensorAboutPageLocators.PICTURE_DEVELOPING_A_VLSI_SYSTEM)
        self.driver.execute_script("arguments[0].scrollIntoView();", picture)
        height = picture.get_attribute('height')
        width = picture.get_attribute('width')
        all_height.append(int(height))
        all_width.append(int(width))

        picture = self.driver.find_element(
            *TensorAboutPageLocators.PICTURE_PROMOTE_SERVICES)
        height = picture.get_attribute('height')
        width = picture.get_attribute('width')
        all_height.append(int(height))
        all_width.append(int(width))

        picture = self.driver.find_element(
            *TensorAboutPageLocators.PICTURE_CREATE_INFRASTRUCTURE)
        height = picture.get_attribute('height')
        width = picture.get_attribute('width')
        all_height.append(int(height))
        all_width.append(int(width))

        picture = self.driver.find_element(
            *TensorAboutPageLocators.PICTURE_CREATE_INFRASTRUCTURE)
        height = picture.get_attribute('height')
        width = picture.get_attribute('width')
        all_height.append(int(height))
        all_width.append(int(width))

        assert len(set(all_height)) == 1, 'Your height is different'
        assert len(set(all_width)) == 1, 'Your width is different'

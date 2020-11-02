from gui_tests.pages.BasePage import BasePage
from gui_tests.locators.PositionPageLocators import PositionPageLocators


class PositionPage(BasePage):

    def click_apply_button(self):
        self.wait_for_element_clickable(PositionPageLocators.APPLY_BUTTON, 5).click()

    def is_position_page_opened(self):
        return "Quality Assurance" in self.driver.title

    def is_description_displayed(self):
        return self.is_element_present(PositionPageLocators.JOB_DESCRIPTION)

    def are_valid_categories_opened(self, location, position):
        return location.upper() in self.driver.find_element(*PositionPageLocators.DESCRIPTION_LOCATION).text and\
               position.upper() in self.driver.find_element(*PositionPageLocators.DESCRIPTION_POSITION).text

    def are_requirements_displayed(self):
        return self.is_element_present(PositionPageLocators.JOB_REQUIREMENTS)

    def is_apply_button_displayed(self):
        return self.is_element_present(PositionPageLocators.JOB_REQUIREMENTS)

    def is_application_form_opened(self):
        return self.is_element_present(PositionPageLocators.APPLICATION_FORM)
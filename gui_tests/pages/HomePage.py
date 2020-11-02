from gui_tests.pages.BasePage import BasePage
from gui_tests.locators.HomePageLocators import HomePageLocators


class HomePage(BasePage):

    home_page_url = "https://useinsider.com"

    def open_home_page(self):
        self.navigate_to(self.home_page_url)

    def click_careers(self):
        self.wait_for_element_invisible(HomePageLocators.SPINNER, 10)
        self.wait_for_element_clickable(HomePageLocators.CAREER_HEADER_ITEM, 10).click()

    def is_home_page_opened(self):
        return "The First Integrated Growth Management Platform - Insider" in self.driver.title

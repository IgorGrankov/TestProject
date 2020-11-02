import time

from gui_tests.pages.BasePage import BasePage
from gui_tests.locators.CareersPageLocators import CareersPageLocators


class CareersPage(BasePage):
    def is_careers_page_opened(self):
        return "Career - Insider" in self.driver.title

    def scroll_to_opportunities(self):
        self.scroll_to(CareersPageLocators.OPPORTUNITIES_HEADER)

    def open_position_from_results(self, position_number):
        locator="//div[@class='jobs-list']/a[{}]".format(position_number)
        self.driver.find_element_by_xpath(locator).click()

    def filter_job_by_location(self, location):
        self.select_from_dropdown(CareersPageLocators.LOCATIONS_DROPDOWN, location)

    def select_department(self, department):
        self.select_from_dropdown(CareersPageLocators.JOB_DEPARTMENT, department)

    def filter_job_by_location_and_department(self, location, department):
        self.filter_job_by_location(location)
        self.select_department(department)

    def is_culture_section_available(self):
        return self.is_element_present(CareersPageLocators.CULTURE_SECTION)

    def is_locations_section_available(self):
        return self.is_element_present(CareersPageLocators.LOCATIONS_SECTION)

    def is_teams_section_available(self):
        return self.is_element_present(CareersPageLocators.TEAMS_SECTION)

    def is_jobs_section_available(self):
        return self.is_element_present(CareersPageLocators.JOBS_SECTION)

    def is_life_section_available(self):
        return self.is_element_present(CareersPageLocators.LIFE_SECTION)

    def is_jobs_list_opened(self):
        return self.is_element_present(CareersPageLocators.JOBS_LIST)

    def are_departments_correct(self, department):
        return self.are_elements_contain_text(CareersPageLocators.JOBS_DEPARTMENTS, text=department)

    def are_locations_correct(self, locations):
        return self.are_elements_contain_text(CareersPageLocators.JOBS_LOCATIONS, text=locations)

    def are_positions_correct(self, positions):
        return self.are_elements_contain_text(CareersPageLocators.JOBS_TITLES, text=positions)


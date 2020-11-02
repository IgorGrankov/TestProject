import pytest
import unittest
from gui_tests.pages.HomePage import HomePage
from gui_tests.pages.CareersPage import CareersPage
from gui_tests.pages.PositionPage import PositionPage

class TestJobApplication(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, driver):
        self.homePage = HomePage(driver)
        self.careersPage = CareersPage(driver)
        self.positionPage = PositionPage(driver)

    def test_apply_job_flow(self):
        location = "Istanbul, Turkey"
        position = "Quality Assurance"

        self.homePage.open_home_page()
        assert self.homePage.is_home_page_opened(), "Home page is opened"

        self.homePage.click_careers()

        assert self.careersPage.is_careers_page_opened(), "Careers page is opened"
        assert self.careersPage.is_culture_section_available(), "Culture section is available"
        assert self.careersPage.is_locations_section_available(), "Locations section is available"
        assert self.careersPage.is_teams_section_available(), "Teams section is available"
        assert self.careersPage.is_jobs_section_available(), "Jobs section is available"
        assert self.careersPage.is_life_section_available(), "Life section is available"

        self.careersPage.scroll_to_opportunities()
        self.careersPage.filter_job_by_location_and_department(location, position)

        assert self.careersPage.is_jobs_list_opened()
        assert self.careersPage.are_departments_correct(position)
        assert self.careersPage.are_locations_correct(location)
        assert self.careersPage.are_positions_correct(position)

        self.careersPage.open_position_from_results(2)

        assert self.positionPage.is_position_page_opened(), "Position page is opened"
        assert self.positionPage.are_valid_categories_opened(location, position), "Required categories match"
        assert self.positionPage.is_description_displayed(), "Job description is displayed"
        assert self.positionPage.are_requirements_displayed(), "Requirements are displayed"
        assert self.positionPage.is_apply_button_displayed(), "Apply button is dis[layed"

        self.positionPage.click_apply_button()

        assert self.positionPage.is_application_form_opened()




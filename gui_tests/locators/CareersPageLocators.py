from selenium.webdriver.common.by import By


class CareersPageLocators:
    CULTURE_SECTION = (By.ID, "culture")
    LOCATIONS_SECTION = (By.ID, "locations")
    TEAMS_SECTION = (By.ID, "teams")
    JOBS_SECTION = (By.ID, "jobs")
    LIFE_SECTION = (By.ID, "life-at-insider")
    OPPORTUNITIES_HEADER = (By.XPATH, "//h2[text()='CAREER OPPORTUNITIES']")
    LOCATIONS_DROPDOWN = (By.CSS_SELECTOR, ".jobs-locations")
    JOB_DEPARTMENT = (By.CSS_SELECTOR, ".jobs-teams")
    JOBS_LIST = (By.CSS_SELECTOR, ".jobs-list")
    JOBS_DEPARTMENTS = (By.XPATH, "//a[contains(@class, 'job')]/span[2]")
    JOBS_LOCATIONS = (By.XPATH, "//a[contains(@class, 'job')]/span[3]")
    JOBS_TITLES = (By.XPATH, "//a[contains(@class, 'job')]/span[1]")
from selenium.webdriver.common.by import By


class PositionPageLocators:
    JOB_DESCRIPTION = (By.XPATH, "//div[contains(@class, 'section page-centered')][1]")
    JOB_REQUIREMENTS = (By.CSS_SELECTOR, ".posting-requirements")
    APPLY_BUTTON = (By.CSS_SELECTOR, ".template-btn-submit")
    DESCRIPTION_LOCATION = (By.XPATH, "//div[contains(@class, 'posting-category')][1]")
    DESCRIPTION_POSITION = (By.XPATH, "//div[contains(@class, 'posting-category')][2]")
    APPLICATION_FORM = (By.CSS_SELECTOR, ".application-form")
from selenium.webdriver.common.by import By


class HomePageLocators:
    CAREER_HEADER_ITEM = (By.XPATH, "(//a/span[contains(text(), 'CAREER')])[1]")
    SPINNER = (By.CSS_SELECTOR, ".spinner")
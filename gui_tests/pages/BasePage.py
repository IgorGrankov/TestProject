import time
from traceback import print_stack

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element_invisible(self, locator, timeout):
        element = None
        try:
            wait = WebDriverWait(
                self.driver,
                timeout
            )
            element = wait.until(EC.visibility_of_element_located(locator))
        except Exception:
            print_stack()
        return element

    def wait_for_element_visible(self, locator, timeout):
        element = None
        try:
            wait = WebDriverWait(
                self.driver,
                timeout
            )
            element = wait.until(EC.visibility_of_element_located(locator))
        except Exception:
            print_stack()
        return element

    def wait_for_element_present(self, locator, timeout):
        element = None
        try:
            wait = WebDriverWait(
                self.driver,
                timeout
            )
            element = wait.until(EC.presence_of_element_located(locator))
        except Exception:
            print_stack()
        return element

    def wait_for_element_clickable(self, locator, timeout):
        element = None
        try:
            wait = WebDriverWait(
                self.driver,
                timeout
            )
            element = wait.until(EC.element_to_be_clickable(locator))
        except Exception:
            print_stack()
        return element

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def scroll_to(self, locator):
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            self.driver.find_element(*locator),
        )

    def select_from_dropdown(self, locator, item):
        self.wait_for_element_clickable(locator, 2)
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(item)
        # I definitely know that using sleeps is anti-pattern, but
        # in this particular case the filtering is extremely slow and sometimes fails showing wrong results or miss them
        # so this is a good place to raise a defect
        time.sleep(2)

    def are_elements_contain_text(self, locator, text):
        correct = True
        self.wait_for_element_visible(locator, 2)
        try:
            items = self.driver.find_elements(*locator)
        except StaleElementReferenceException:
            time.sleep(5)
            items = self.driver.find_elements(*locator)
        for item in items:
            if text in item.text:
               pass
            else:
               correct = False
        return correct
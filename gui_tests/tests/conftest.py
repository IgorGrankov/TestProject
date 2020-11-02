import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="browser: specify chrome or firefox")

# TODO env OS selection
@pytest.fixture(scope="session", autouse=True)
def driver(request):
    driver = None
    default_wait = 5

    option_value = request.config.option.browser
    if option_value == "chrome":
        options = Options()
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path="gui_tests/drivers/chromedriver-mac", options=options)
    elif option_value == "firefox":
        driver = webdriver.Firefox(executable_path="gui_tests/drivers/geckodriver-mac")
    driver.implicitly_wait(default_wait)
    driver.set_page_load_timeout(default_wait)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['driver']
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)


def take_screenshot(driver, nodeid):
    file_name = f'{nodeid}_{datetime.datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/","_").replace("::","__")
    driver.save_screenshot(file_name)
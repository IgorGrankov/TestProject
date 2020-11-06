import pytest
import datetime
import requests
import os
import platform
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="browser: specify chrome or firefox")

@pytest.fixture(scope="session", autouse=True)
def driver(request):
    driver = None
    default_wait = 15

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    driver_path = os.path.join(cur_dir, "../drivers/chromedriver")

    option_value = request.config.option.browser
    if option_value == "chrome":
        download_chromedriver()
        options = Options()
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=driver_path, options=options)
    elif option_value == "firefox":
        driver = webdriver.Firefox(executable_path="gui_tests/drivers/geckodriver")
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


def download_chromedriver():
    url = None
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    print(cur_dir)
    drivers_dir = os.path.join(cur_dir, "../drivers/")
    destination_dir = "../drivers/chromedriver.zip"
    chromedriver_destination = os.path.join(cur_dir, destination_dir)
    files = os.listdir(drivers_dir)
    print(files)

    if 'chromedriver' not in drivers_dir:
        if platform.system() == 'Darwin':
            url = "https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_mac64.zip"
        elif platform.system() == 'Windows':
            url = "https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_win32.zip"
        elif platform.system() == 'Linux':
            url = "https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip"

        r = requests.get(url, allow_redirects=True)
        open(chromedriver_destination, 'wb').write(r.content)
        with zipfile.ZipFile(chromedriver_destination, 'r') as zip_ref:
            zip_ref.extractall(drivers_dir)

        os.chmod(os.path.join(drivers_dir, "chromedriver"), 0o755)
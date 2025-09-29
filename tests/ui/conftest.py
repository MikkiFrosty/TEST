from selene import browser

# --- PYTHONPATH guard: ensure project root on sys.path ---
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
# ---------------------------------------------------------


import os
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
# from utils import attach
import allure
import os, sys

load_dotenv()

@pytest.fixture(autouse=True, scope='function')
def setup_browser():
    browser.config.base_url = "https://finance.ozon.ru"
    browser.config.window_width = 1280
    browser.config.window_height = 800
    yield
    browser.quit()
# @pytest.fixture(autouse=True, scope='function')
# def setup_browser():
#     host = os.getenv('SELENOID_URL')
#     login = os.getenv('SELENOID_LOGIN')
#     password = os.getenv('SELENOID_PASS')
#
#     # чтобы не было host='none'
#     assert host and login and password, 'ENV missing: SELENOID_URL/LOGIN/PASS'
#
#     options = Options()
#     options.set_capability('browserName', 'chrome')
#     options.set_capability('browserVersion', '128.0')
#     options.set_capability('selenoid:options', {'enableVNC': True, 'enableVideo': False})
#
#     browser.driver = webdriver.Remote(
#         command_executor=f'https://{login}:{password}@{host}/wd/hub',
#         options=options,
#     )

    browser.config.driver = browser.driver
    browser.config.base_url = 'https://finance.ozon.ru'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 6

    # try:
    #     yield browser
    # finally:
    #     with allure.step('Tear down'):
    #         attach.add_screenshot(browser)
    #         attach.add_logs(browser)
    #         attach.add_html(browser)
    #         attach.add_video(browser)
    #     browser.quit()
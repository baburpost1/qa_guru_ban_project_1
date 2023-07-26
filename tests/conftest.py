import pytest
from selene.core.configuration import Config
from selene.support.shared import browser


@pytest.fixture()
def set_window_size():
    Config.window_width = 2500
    Config.window_height = 2500


@pytest.fixture()
def open_google(set_window_size):
    browser.open('https://google.com')

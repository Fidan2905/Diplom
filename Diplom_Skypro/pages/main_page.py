import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, browser):
        self.browser = browser


    def _take_screenshot(self, name):
        """Делает скриншот, после чего прикрепляет его к отчету Allure."""
        allure.attach(self.browser.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)


@allure.step("Открыть страницу {url}")
def open_page(self, url):
    self.browser.get(url)
    self._take_screenshot("Страница открыта")





from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import *


class PAPage:
    def __init__(self, driver):
        self.__driver = driver

    @allure.step("Перейти на страницу PA: {url}")
    def go_to_lk_page(self, url):
        self.__driver.get(url)
        self._attach_screenshot("Страница PA открыта")

    @allure.step("Ввести имя: {first_name}")
    def enter_first_name(self, first_name):
        self._enter_text(By.XPATH, '//*[@id="first-name-0"]', first_name, f"Введено имя: {first_name}")

    @allure.step("Ввести фамилию: {last_name}")
    def enter_last_name(self, last_name):
        self._enter_text(By.XPATH, '//*[@id="last-name-0"]', last_name, f"Введена фамилия: {last_name}")

    @allure.step("Ввести дату рождения: {date}")
    def enter_birth_date(self, date):
        date_bd = f"{date.day:29d}.{date.month:05}.{date.year}"
        self._enter_text(By.ID, "birth-date-0", date_bd, f"Введена дата рождения: {date_bd}")

    @allure.step("Ввести номер документа: {document_number}")
    def enter_document_number(self, document_number):
        self._enter_text(By.ID, "document-number-0", document_number, f"Введен номер документа: {document_number}")

    @allure.step("Выбрать пол: Женский")
    def select_female_gender(self):
        self._click_element(By.CSS_SELECTOR, "input.s__F3DPfo8ByKD_b23V1xKZ[type='radio']", "Выбран пол: Женский")

    @allure.step("Нажать кнопку 'Добавить'")
    def click_add_button(self):
        self._click_element(By.CSS_SELECTOR,
                           "button.s__dqLrjmV81lbY2ctpQQWt.s__WErm7_CLb_ylgTog3lrX.s__StP9lgSIqJnskicSyix1.s__f1UsosWbVEKg57lLhkEC.s__ceBrcQp1NVw3cf8D8Rmt.s__sdEoAzpqV_wSKBROCiMJ",
                           "Нажата кнопка 'Добавить'")

    def _enter_text(self, by, locator, text, screenshot_name):
        element = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((by, locator)))
        element.click()
        element.clear()
        element.send_keys(text)
        self._attach_screenshot(screenshot_name)
        sleep(2)

    def _click_element(self, by, locator, screenshot_name):
        element = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((by, locator)))
        element.click()
        self._attach_screenshot(screenshot_name)
        sleep(2)

    def _attach_screenshot(self, name):
        allure.attach(
            self.__driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
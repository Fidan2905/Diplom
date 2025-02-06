from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Optional

class MainPage:

    # Селекторы
    ORIGIN_INPUT = (By.ID, "avia_form_origin-input")
    DESTINATION_INPUT = (By.ID, "avia_form_destination-input")
    DEPARTURE_CALENDAR_ICON = (By.CSS_SELECTOR, '[data-test-id="departure-calendar-icon"]')
    DATE_SELECTOR = (By.CSS_SELECTOR, '[data-test-id="date-{}"]')
    PASSENGERS_FIELD = (By.CSS_SELECTOR, '[data-test-id="passengers-field"]')
    INCREASE_BUTTON = (By.CSS_SELECTOR, '[data-test-id="increase-button"]')
    TRIP_CLASS_F = (By.CSS_SELECTOR, '[data-test-id="trip-class-F"]')
    TRIP_CLASS_W = (By.CSS_SELECTOR, '[data-test-id="trip-class-W"]')
    FORM_SUBMIT = (By.CSS_SELECTOR, '[data-test-id="form-submit"]')
    PASSENGERS_QUANTITY = (By.XPATH, "(//div[@aria-label='passengers'])[1]")
    TRIP_CLASS = (By.XPATH, "(//div[@data-test-id='trip-class'])[1]")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://www.aviasales.ru/")
        self.driver.maximize_window()

    def fill_origin(self, origin: str) -> None:
        """Заполнение поля Откуда"""
        element_origin = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ORIGIN_INPUT)
        )
        element_origin.clear()
        element_origin.send_keys(origin)

    def fill_destination(self, destination: str) -> None:
        """Заполнение поля Куда"""
        element_destination = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DESTINATION_INPUT)
        )
        element_destination.clear()
        element_destination.send_keys(destination)

    def open_calendar(self) -> None:
        """Открытие календаря"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DEPARTURE_CALENDAR_ICON)
        ).click()

    def choose_date(self, date: str) -> None:
        """Выбор даты"""
        date_selector = (self.DATE_SELECTOR[0], self.DATE_SELECTOR[1].format(date))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(date_selector)
        ).click()

    def choose_passengers_quantity(self, quantity: int = 1) -> None:
        """Выбор количества пассажиров"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PASSENGERS_FIELD)
        ).click()
        for _ in range(quantity):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.INCREASE_BUTTON)
            ).click()

    def choose_trip_class(self, trip_class: str) -> None:
        """Выбор класса (F - первый класс, W - комфорт)"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PASSENGERS_FIELD)
        ).click()
        if trip_class == "F":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.TRIP_CLASS_F)
            ).click()
        elif trip_class == "W":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.TRIP_CLASS_W)
            ).click()
        else:
            raise ValueError("Неверный класс. Допустимые значения: 'F' или 'W'.")

    def click_search(self) -> None:
        """Нажать кнопку Найти"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FORM_SUBMIT)
        ).click()

    def get_origin_value(self) -> str:
        """Получение значения поля Откуда"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ORIGIN_INPUT)
        ).get_attribute("value")

    def get_destination_value(self) -> str:
        """Получение значения поля Куда"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DESTINATION_INPUT)
        ).get_attribute("value")

    def get_passengers_quantity(self) -> str:
        """Получение количества пассажиров"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PASSENGERS_QUANTITY)
        ).text

    def get_trip_class(self) -> str:
        """Получение класса"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TRIP_CLASS)
        ).text
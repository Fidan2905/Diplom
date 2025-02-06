from time import sleep
import allure
from selenium.webdriver.common.by import By
from datetime import datetime
from pages.main_page import MainPage
from settings import *

@allure.epic("Авиасейлс - поиск дешевых билетов")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(url="https://www.aviasales.ru/", name="Авиасейлс")


class TestUi:
    """Сервис Авиасейлс предоставляет возможность подобрать авиабилеты
    на различные направления и даты. Пользователи могут выбирать из множества
    вариантов рейсов, включая как прямые, так и сложные маршруты с пересадками.
    Кроме того, доступны билеты разных ценовых категорий, что позволяет найти
    подходящий вариант по бюджету"""


    @allure.title("Поиск авиабилетов Бку-Стамбул")
    def test_search_tickets_baku_istanbul(self, browser):
        departure_date = datetime(2025, 4, 8)
        main_page = MainPage(browser)

        with allure.step("Открываем браузер Chrome по адресу https://www.aviasales.ru"):
            main_page.open_page(base_url_ui)

        with allure.step("Вводим город отправления"):
            main_page.enter_origin_city(departure_city)

        with allure.step("Ввод города назначения"):
            main_page.enter_destination_city(destination_city)

        with allure.step("Выбор даты вылета"):
            main_page.select_departure_date(departure_date)

        with allure.step("Выбор 'обратно не нужен'"):
            main_page.click_no_return_needed()

        with allure.step("Нажать кнопку Найти билеты"):
            main_page.search_for_tickets()

        with allure.step("Вернуться назад на Авиасейлс"):
            browser.back()

        with allure.step('Делаем скриншот для контроля'):
            current_time = int(datetime.now().timestamp())
            filename = f"./QA_{browser.name}_{current_time}.png"
            browser.save_screenshot(filename)

    @allure.title("Ввод данных для покупки билетов в ЛК")
    def test_doc_pa(browser):
        doc_lk = PA_Page(browser)
        birth_date = datetime(2004, 5, 29)

        # Открываем страницу PA
        browser.get(base_url_pa)
        sleep(50)

        # Ввод корректных данных
        doc_pa.enter_first_name(first_name)
        doc_pa.enter_last_name(last_name)
        doc_pa.enter_birth_date(birth_date)
        doc_pa.enter_document_number(document_number)

        # Проверка корректности введенных данных
        assert browser.find_element(By.ID, "first_name_0").get_attribute("value") == first_name.upper()
        assert browser.find_element(By.ID, "last_name_0").get_attribute("value") == last_name.upper()
        allure.attach(browser.get_screenshot_as_png(), name="screenshot_2", attachment_type=allure.attachment_type.PNG)

        # Выбор пола и отправка формы
        doc_lk.radio_button_male()
        doc_lk.enter_send()
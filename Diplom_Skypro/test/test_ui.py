import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

from pages.main_page import MainPage

@allure.title("Проверка открытия страницы aviasales.ru и автоматическое заполнение города")
@allure.severity("medium")
def test_open_page():
    current_city = "Баку" #Подставить город, где вы находитесь (с аэропортом)
    with allure.step("Открыть страницу"):
        main_page = MainPage(driver)
    with allure.step("Проверка автоматического заполнения города"):
        assert driver.find_element(By.ID, "avia_form_origin-input").get_attribute("value") == current_city
    driver.quit()

@allure.title("Проверка того, что открывается страница https://ostrovok.ru/ при поиске билетов")
@allure.severity("medium")
def test_hotels():
    main_page = MainPage(driver)
    with allure.step("Заполнить город отправления"):
        main_page.fill_origin("Баку")
    with allure.step("Заполнить город назначения"):
        main_page.fill_destination("Стамбул")
    main_page.open_calendar()
    main_page.choose_date("02.03.2025")
    main_page.click_search()
    with allure.step("Проверка того, что открывается страница https://ostrovok.ru/ при поиске билетов"):
        assert "https://www.aviasales.ru/" in driver.current_url

@allure.title("Проверка загаловка страницы")
@allure.severity("medium")
def test_text():
    main_page = MainPage(driver)
    expected_text = "Тут покупают дешёвые авиабилеты"
    header = driver.find_element(By.CSS_SELECTOR, "h1.header__title")
    with allure.step("Проверка того, что в заголовке указан нужный текст"):
        assert header.text == expected_text

@allure.title("Негативный тест на проверку заполнения без города")
@allure.severity("critical")
def test_negative_destination():
    main_page = MainPage(driver)
    main_page.click_search()
    element = driver.find_element(By.XPATH, '//div[text()="Укажите город прибытия"]')
    with allure.step("Проверка того, что незаполненное поле Куда подчвечивается"):
        assert element.is_displayed()

@allure.title("Негативный тест на проверку заполнения без даты")
@allure.severity("critical")
def test_negative_date():
    main_page = MainPage(driver)
    main_page.click_search()
    element = driver.find_element(By.XPATH, '//div[text()="Укажите дату"]')
    with allure.step("Проверка того, что незаполненное поле Дата подчвечивается"):
        assert element.is_displayed()

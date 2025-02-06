import pytest
import allure
from settings import *
from pages.api_page import AviasalesAPI  # Импортируйте ваш класс AviasalesAPI


# Инициализация объекта API
@pytest.fixture(scope="module")
def api():
    return AviasalesAPI()

# Тест для метода get_cheapest_tickets
@allure.feature("Поиск самых дешевых авиабилетов")
@allure.story("Проверка метода get_cheapest_tickets")
def test_get_cheapest_tickets(api):


    with allure.step("Запрос самых дешевых билетов"):
        response = api.get_cheapest_tickets(origin, destination, depart_date, return_date)

    with allure.step("Проверка ответа"):
        assert isinstance(response, dict), "Ответ должен быть словарем"
        assert "data" in response, "В ответе должен быть ключ 'data'"
        assert len(response["data"]) > 0, "Список билетов не должен быть пустым"

# Тест для метода get_monthly_prices
@allure.feature("Получение цен на авиабилеты за месяц")
@allure.story("Проверка метода get_monthly_prices")
def test_get_monthly_prices(api):

    with allure.step("Запрос цен на билеты за месяц"):
        response = api.get_monthly_prices(origin, destination)

    with allure.step("Проверка ответа"):
        assert isinstance(response, dict), "Ответ должен быть словарем"
        assert "data" in response, "В ответе должен быть ключ 'data'"
        assert len(response["data"]) > 0, "Список цен не должен быть пустым"

# Тест для метода direct_tickets
@allure.feature("Поиск прямых рейсов")
@allure.story("Проверка метода direct_tickets")
def test_direct_tickets(api):


    with allure.step("Запрос прямых рейсов"):
        response = api.direct_tickets(origin, destination, depart_date, return_date)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200, "Статус код должен быть 200"
        assert isinstance(response.json(), dict), "Ответ должен быть словарем"

# Тест для метода city_directions
@allure.feature("Популярные маршруты авиакомпаний")
@allure.story("Проверка метода city_directions")
def test_city_directions(api):

    with allure.step("Запрос популярных маршрутов"):
        response = api.city_directions(origin, currency)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200, "Статус код должен быть 200"
        assert isinstance(response.json(), dict), "Ответ должен быть словарем"

# Тест для метода airline_directions
@allure.feature("Популярные маршруты авиакомпаний")
@allure.story("Проверка метода airline_directions")
def test_airline_directions(api):

    limit = "5"

    with allure.step("Запрос маршрутов авиакомпании"):
        response = api.airline_directions(airline_code, limit)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200, "Статус код должен быть 200"
        assert isinstance(response.json(), dict), "Ответ должен быть словарем"

# Тест для метода get_popular_destinations
@allure.feature("Поиск билетов в популярные направления")
@allure.story("Проверка метода get_popular_destinations")
def test_get_popular_destinations(api):

    with allure.step("Запрос популярных направлений"):
        response = api.get_popular_destinations(origin, currency)

    with allure.step("Проверка ответа"):
        assert isinstance(response, dict), "Ответ должен быть словарем"
        assert "data" in response, "В ответе должен быть ключ 'data'"
        assert len(response["data"]) > 0, "Список направлений не должен быть пустым"
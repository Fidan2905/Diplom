import requests
import allure
from settings import *


@allure.epic("Авиасейлс - поиск дешевых билетов")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://www.aviasales.ru/", name="Авиасейлс")


class AviasalesAPI:
    """Класс для взаимодействия с API Aviasales. Предоставляет методы для поиска авиабилетов,
    получения цен за месяц, поиск прямых рейсов, поиска маршрутов популярных авиакомпаний и билетов в популярные
    направления."""

    def __init__(self):
        self.base_url = base_url
        self.token = token
        self.headers = {'X-Access-Token': token}
        #self.session = requests.Session()


    @allure.step("Поиск самых дешевых авиабилетов из {origin} в {destination} на дату {depart_date}")
    def get_cheapest_tickets(self, origin: str, destination: str, depart_date: str, return_date: str,
                            currency: str = "RUB"):
        """Ищет самые дешевые авиабилеты на указанные даты."""
        params = {
            "origin": origin,
            "destination": destination,
            "depart_date": depart_date,
            "return_date": return_date,
            "currency": currency
        }
        path = self.base_url + "prices_for_dates"
        response = requests.get(path, headers=self.headers, params=params)
        return response.json()


    @allure.step("Получение цен на авиабилеты за месяц из {origin} в {destination}")
    def get_monthly_prices(self, origin: str, destination: str, currency: str = "AZN"):
        """Получает цены на авиабилеты за месяц."""
        params = {
            "origin": origin,
            "destination": destination,
            "currency": currency
        }
        path = base_url_2 + "prices/month-matrix"
        response = requests.get(path, headers=self.headers, params=params)
        return response.json()


    @allure.step("Поиск прямых рейсов из {origin} в {destination} на дату {depart_date}")
    def direct_tickets(self, origin: str, destination: str, depart_date: str, return_date: str):
        """Ищет прямые рейсы."""
        params = {
            "origin": origin,
            "destination": destination,
            "depart_date": depart_date,
            "return_date": return_date,
        }
        path = base_url_3 + "city-directions"
        response = requests.get(path, headers=self.headers, params=params)
        return response


    @allure.step("Популярные маршруты авиакомпаний из {origin}")
    def city_directions(self, origin: str, currency: str):
        """Ищет билеты на каждый день указанного месяца."""
        params = {
            "origin": origin,
            "currency": currency,
            "airline_code": "J2"
        }
        path = base_url_3 + "airline-directions"
        response = requests.get(path, headers=self.headers, params=params)
        return response


    @allure.step("Популярные маршруты авиакомпаний")
    def airline_directions(self, airline_code: str, limit: str):
        """Ищет билеты на каждый день указанного месяца."""
        params = {
            "airline_code": airline_code,
            "limit": limit
        }
        path = base_url_3 + "/airline-directions"
        response = requests.get(path, headers=self.headers, params=params)
        return response


    @allure.step("Поиск билетов в популярные направления из {origin}")
    def get_popular_destinations(self, origin: str, currency: str = "AZN"):
        """Ищет билеты в популярные направления из указанного города."""
        params = {
            "origin": origin,
            "currency": currency
        }
        path = base_url_3 + "city-directions"
        response = requests.get(path, headers=self.headers, params=params)
        return response.json()
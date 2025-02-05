import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Авиасейлс - поиск дешевых билетов")  # Группировка тестов по эпику
@allure.severity(allure.severity_level.CRITICAL)  # Указание уровня критичности тестов
@allure.link("https://www.aviasales.ru/", name="Авиасейлс")  # Ссылка на тестируемый ресурс


class BasePage:
    """Базовый класс для работы со страницами в веб-приложении.
    Содержит общие методы, применяемые для взаимодействия с элементами страницы."""

    def __init__(self, driver):
        self.driver = driver  # Экземпляр веб-драйвера
        self.wait = WebDriverWait(driver, 10)  # Ожидание элементов в течение 10 секунд


    def is_element_present(self, locator):
        """Проверяет наличие элемента на странице.
        :param locator: Кортеж, содержащий стратегию локатора и его значение (например, (By.ID, 'element_id')).
        :return: True, если элемент найден, иначе False."""
        try:
            self.wait.until(EC.presence_of_element_located(locator))  # Ожидание появления элемента
            return True
        except TimeoutException:  # Если элемент не найден в течение заданного времени
            return False
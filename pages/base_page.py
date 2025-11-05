import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Перейти по URL: {url}')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Найти элемент с ожиданием: {locator}')
    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на элемент: {locator}')
    def click_to_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ввести текст "{text}" в элемент: {locator}')
    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст из элемента: {locator}')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролл к элементу: {locator}')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Форматировать локатор с номером: {locator_template}, номер: {num}')
    def format_locator(self, locator_template, num):
        method, locator = locator_template
        locator = locator.format(num)
        return method, locator

    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_tab(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
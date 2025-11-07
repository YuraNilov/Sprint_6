import allure
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.general_locators import GeneralLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Принять куки')
    def accept_cookies(self):
        try:
            self.click_to_element(GeneralLocators.COOKIE_BUTTON)
        except TimeoutException:
            pass

    @allure.step('Клик на вопрос номер {num}')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        
        question_element = self.find_element_with_wait(locator_q_formatted)
        self.scroll_to_element(locator_q_formatted)
        
        question_element.click()

    @allure.step('Получение ответа на вопрос номер {num}')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверяем вопрос и ответ номер {num}')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)

    @allure.step('Клик на логотип Самоката')
    def click_scooter_logo(self):
        self.click_to_element(GeneralLocators.SCOOTER_LOGO)

    @allure.step('Клик на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_to_element(GeneralLocators.YANDEX_LOGO)

    @allure.step('Проверить наличие изображения самоката')
    def check_scooter_image_present(self):
        return self.find_element_with_wait(MainPageLocators.SCOOTER_IMAGE).is_displayed()

    @allure.step('Клик на верхнюю кнопку заказа')
    def click_top_order_button(self):
        self.click_to_element(GeneralLocators.ORDER_BUTTON_TOP)

    @allure.step('Клик на нижнюю кнопку заказа')
    def click_bottom_order_button(self):
        button_element = self.find_element_with_wait(GeneralLocators.ORDER_BUTTON_BOTTOM)
        try:
            button_element.click()
        except ElementClickInterceptedException:
            # Если не сработал обычный клик - используем JavaScript клик
            self.driver.execute_script("arguments[0].click();", button_element)

    @allure.step('Дождаться кнопки поиска на Дзене')
    def wait_for_dzen_search_button(self):
        search_button_locator = (By.XPATH, "//button[text()='Найти']")
        return self.wait_for_element(search_button_locator)
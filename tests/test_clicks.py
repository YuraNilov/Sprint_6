import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urls import URL_MAIN_PAGE, TRACK_PAGE_ENDPOINT
from pages.main_page import MainPage


@allure.epic('Тесты переходов по логотипам')
class TestClicks:
    @allure.title('Переход по логотипу Самоката со страницы заказа')
    def test_click_scooter_logo_from_order_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(URL_MAIN_PAGE + TRACK_PAGE_ENDPOINT)
        main_page.accept_cookies()
        
        main_page.click_scooter_logo()
        assert main_page.check_scooter_image_present()

    @allure.title('Переход по логотипу Яндекса с главной страницы')
    def test_click_yandex_logo_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(URL_MAIN_PAGE)
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        
        search_button = main_page.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Найти']"))
        )
        
        assert search_button.is_displayed()
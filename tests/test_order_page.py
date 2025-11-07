import pytest
import allure
from data import OrderData
from urls import URL_MAIN_PAGE
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.epic('Тесты оформления заказа')
class TestOrderPage:
    @pytest.mark.parametrize('order_button,order_data', [
        ("top", OrderData.ORDER_DATA_1),
        ("bottom", OrderData.ORDER_DATA_2)
    ])
    @allure.title('Оформление заказа')
    def test_create_order(self, driver, order_button, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.go_to_url(URL_MAIN_PAGE)
        main_page.accept_cookies()
        
        if order_button == "bottom":
            main_page.click_bottom_order_button()
        else:
            main_page.click_top_order_button()
        
        is_success = order_page.complete_order_process(order_data)
        assert is_success
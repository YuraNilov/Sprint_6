import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнить данные клиента')
    def fill_first_page(self, order_data):
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, order_data["name"])
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD, order_data["surname"])
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, order_data["address"])
        
        self.click_to_element(OrderPageLocators.METRO_FIELD)
        station_locator = (OrderPageLocators.METRO_STATION_OPTION[0],
                          OrderPageLocators.METRO_STATION_OPTION[1].format(order_data["metro_station"]))
        self.click_to_element(station_locator)
        
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD, order_data["phone"])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить данные аренды')
    def fill_second_page(self, order_data):
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        
        date_option_locator = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='" + order_data["date"] + "']")
        self.click_to_element(date_option_locator)
        
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        rental_locator = (OrderPageLocators.RENTAL_OPTION[0],
                         OrderPageLocators.RENTAL_OPTION[1].format(order_data["rental_period"]))
        self.click_to_element(rental_locator)
        
        if order_data["color"] == "black":
            self.click_to_element(OrderPageLocators.COLOR_BLACK)
        else:
            self.click_to_element(OrderPageLocators.COLOR_GREY)
        
        self.add_text_to_element(OrderPageLocators.COMMENT_FIELD, order_data["comment"])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        confirm_button = self.find_element_with_wait(OrderPageLocators.CONFIRM_YES_BUTTON)
        try:
            confirm_button.click()
        except ElementClickInterceptedException:
            # Если не сработал обычный клик - используем JavaScript клик
            self.driver.execute_script("arguments[0].click();", confirm_button)

    @allure.step('Проверить, что окно с сообщением об успешном создании заказа отображается')
    def is_success_modal_displayed(self):
        return self.find_element_with_wait(OrderPageLocators.SUCCESS_MODAL).is_displayed()

    @allure.step('Выполнить полный процесс заказа')
    def complete_order_process(self, order_data):
        self.fill_first_page(order_data)
        self.fill_second_page(order_data)
        self.confirm_order()
        return self.is_success_modal_displayed()
from selenium.webdriver.common.by import By


class GeneralLocators:
    
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    # Кнопки Заказать на главной странице
    ORDER_BUTTON_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")
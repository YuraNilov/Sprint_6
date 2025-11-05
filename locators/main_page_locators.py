from selenium.webdriver.common.by import By


class MainPageLocators:
    
    QUESTION_LOCATOR = (By.ID, "accordion__heading-{}")
    ANSWER_LOCATOR = (By.ID, "accordion__panel-{}")
    QUESTION_LOCATOR_TO_SCROLL = (By.ID, "accordion__heading-7")
    
    # Элементы для подтверждения переходов
    SCOOTER_IMAGE = (By.XPATH, "//img[@alt='Scooter blueprint']")
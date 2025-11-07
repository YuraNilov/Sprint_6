import pytest
import allure
from data import FAQData, QUESTION_TITLES
from urls import URL_MAIN_PAGE
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.epic('Тесты главной страницы')
class TestMainPage:
    @pytest.mark.parametrize(
        'question_num, question_number, question_title', 
        [(i, i + 1, QUESTION_TITLES[i]) for i in range(8)]
    )
    @allure.title('FAQ {question_number}: {question_title}')
    def test_questions_and_answers(self, driver, question_num, question_number, question_title):
        main_page = MainPage(driver)
        main_page.go_to_url(URL_MAIN_PAGE)
        main_page.accept_cookies()
        
        main_page.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        actual_answer = main_page.check_question_and_answer(question_num)
        expected_answer = FAQData.QUESTIONS_AND_ANSWERS[question_num]
        
        assert actual_answer == expected_answer
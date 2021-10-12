import logging
from locators.login_page_locator import BasePageLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class GooglePage(BasePage):

    def search_fields(self):
        """Функция заполнения поля поиска и нажатия на enter"""
        element = self.find_element(BasePageLocators.INPUT)
        element_2 = self.fill_element(element, "Калькулятор")
        logger.info(f"Вводим слово {element_2.text}")
        self.enter_element(element_2)

    def fill_search_field(self):
        """Функция заполнения поля поиска"""
        element = self.find_element(BasePageLocators.INPUT)
        self.fill_element(element, "Калькулятор")
        logger.info(f"Вводим слово {'Калькулятор'}")

    def click_on_button(self):
        element = self.find_element(BasePageLocators.CLICK)
        self.click_element(element)
        element_2 = self.find_elements(BasePageLocators.BUTTON)[1]
        self.click_element(element_2)

    def click_on_number_one(self):
        element = self.find_clickable_element(BasePageLocators.ONE)
        logger.info(f"Вводим {element.text}")
        self.click_element(element)

    def click_on_number_two(self):
        element = self.find_clickable_element(BasePageLocators.TWO)
        logger.info(f"Вводим {element.text}")
        self.click_element(element)

    def click_on_number_three(self):
        element = self.find_clickable_element(BasePageLocators.THREE)
        logger.info(f"Вводим {element.text}")
        self.click_element(element)

    def click_on_number_multiplication(self):
        element = self.find_clickable_element(BasePageLocators.MULTIPLICATION)
        logger.info(f"Вводим {element.text}")
        self.click_element(element)

    def click_on_number_minus(self):
        element = self.find_clickable_element(BasePageLocators.MINUS)
        logger.info(f"Вводим {element.text}")
        self.click_element(element)

    def click_on_number_plus(self):
        element = self.find_clickable_element(BasePageLocators.PLUS)
        logger.info(f"Вводим {element.text}")
        self.click_element(element)

    def click_on_equally(self):
        element = self.find_clickable_element(BasePageLocators.EQUALLY)
        logger.info(f"Вводим {element.text}")
        self.click_element(element)

    def calculations(self):
        self.click_on_number_one()
        self.click_on_number_multiplication()
        self.click_on_number_two()
        self.click_on_number_minus()
        self.click_on_number_three()
        self.click_on_number_plus()
        self.click_on_number_one()
        self.click_on_equally()

    def calculation_result(self):
        return self.find_element(BasePageLocators.ZERO).text

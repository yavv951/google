#from selenium.webdriver.remote.webelement import WebElement
import logging
from locators.login_page_locator import BasePageLocators
from pages.base_page import BasePage

logger = logging.getLogger("moodle")


class GooglePage(BasePage):

    def search_fields(self):
        element = self.find_element(BasePageLocators.INPUT)
        element_2 = self.fill_element(element, "Калькулятор")
        self.enter_element(element_2)

    def fill_search_field(self):
        element = self.find_element(BasePageLocators.INPUT)
        self.fill_element(element, "Калькулятор")

    def click_on_button(self):
        element = self.find_element(BasePageLocators.CLICK)
        self.click_element(element)
        element_2 = self.find_elements(BasePageLocators.BUTTON)[1]
        self.click_element(element_2)

    def click_on_number_one(self):
        element = self.find_clickable_element(BasePageLocators.ONE)
        self.click_element(element)

    def click_on_number_two(self):
        element = self.find_clickable_element(BasePageLocators.TWO)
        self.click_element(element)

    def click_on_number_three(self):
        element = self.find_clickable_element(BasePageLocators.THREE)
        self.click_element(element)

    def click_on_number_multiplication(self):
        element = self.find_clickable_element(BasePageLocators.MULTIPLICATION)
        self.click_element(element)

    def click_on_number_minus(self):
        element = self.find_clickable_element(BasePageLocators.MINUS)
        self.click_element(element)

    def click_on_number_plus(self):
        element = self.find_clickable_element(BasePageLocators.PLUS)
        self.click_element(element)

    def click_on_equally(self):
        element = self.find_clickable_element(BasePageLocators.EQULLY)
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
        self.find_element(BasePageLocators.CLICK)



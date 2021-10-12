from selenium.webdriver.common.by import By


class BasePageLocators:
    INPUT = (By.NAME, "q")
    BUTTON = (By.CLASS_NAME, "gNO89b")
    CLICK = (By.CLASS_NAME, "gb_pa")
    ONE = (By.XPATH, "//div[text()='1']")
    TWO = (By.XPATH, "//div[text()='2']")
    THREE = (By.XPATH, "//div[text()='3']")
    MULTIPLICATION = (By.XPATH, "//div[text()='×']")
    MINUS = (By.XPATH, "//*[text()='−']")
    PLUS = (By.XPATH, "//*[text()='+']")
    EQUALLY = (By.XPATH, "//*[text()='=']")
    ZERO = (By.ID, "cwos")
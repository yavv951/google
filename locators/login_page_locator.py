from selenium.webdriver.common.by import By


class BasePageLocators:
    # поле поиска
    INPUT = (By.NAME, "q")
    BUTTON = (By.CLASS_NAME, "gNO89b")
    CLICK = (By.CLASS_NAME, "gb_pa")
    ONE = (By.XPATH, "//div[text()='1']")
    TWO = (By.XPATH, "//div[text()='2']")
    THREE = (By.XPATH, "//div[text()='3']")
    MULTIPLICATION = (By.XPATH, "//div[text()='×']")
    MINUS = (By.XPATH, "//*[text()='−']")
    PLUS = (By.XPATH, "//*[text()='+']")
    EQULLY = (By.XPATH, "//*[text()='=']")
    ZERO = (By.CLASS_NAME, "z7BZJb XSNERd")

    # таблица с подсказками
    TABLE_HINTS = (By.CLASS_NAME, "visibility_of_element_located")
    TENSOR_WEBSITE = (By.XPATH, "//*[text()='tensor.ru']")
    BUTTON_INPUT = (By.CLASS_NAME, "button_theme_search")
    SEARCH_RESULTS = (By.CLASS_NAME, "mini-suggest__item_type_fulltext")
    IMAGE_BUTTON = (By.XPATH, "//*[text()='Картинки']")
    DEVELOPMENT_SOFTWARE = (By.XPATH, "//*[text()='О компании']")
    # картинки
    IMAGE = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    IMAGE_TEXT = (By.CLASS_NAME, 'PopularRequestList-SearchText')
    TEXT = (By.NAME, "Text")
    INPUT_TEXT = (By.CLASS_NAME, 'input__control')
    GALLERY_IMAGE = (By.CLASS_NAME, "MMImage-Preview")
    FIRST_IMAGE = (By.CLASS_NAME, "serp-item__link")
    PREV_IMAGE = (By.CLASS_NAME, "CircleButton_type_prev")
    NEXT_IMAGE = (By.CLASS_NAME, "CircleButton_type_next")

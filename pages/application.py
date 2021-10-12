import logging

from selenium.webdriver.common.keys import Keys

from pages.main_page import GooglePage

logger = logging.getLogger("moodle")


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.google = GooglePage(self)

    def quit(self):
        self.driver.quit()

    def open_main_page(self):
        logger.info("open " + self.url)
        self.driver.get(self.url)

    def switch_to_window(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    def refresh(self):
        self.driver.refresh()

    def get_attribute_src(self):
        self.driver.get_attribute("src")


import time

import pytest
from common.constants import LoginConstants



class TestYandex:
    def test_yandex_input(self, app):
        """
        Steps
        1. Open Google page
        2. Enter the word “Calculator” in the search box
        3. Click on button search
        4. Calculate « 1 * 2 - 3 + 1 »

        """
        app.open_main_page()
        app.google.fill_search_field()
        app.google.click_on_button()
        app.google.calculations()

        #app.google.click_on_button()
        assert 0 in app.google.calculation_result()
        time.sleep(3)


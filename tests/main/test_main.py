import logging

from common.constants import LoginConstants

logger = logging.getLogger(__name__)


class TestGoogle:
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
        logger.info(f" {LoginConstants.ANSWER} == {app.google.calculation_result()}")
        assert LoginConstants.ANSWER == app.google.calculation_result()

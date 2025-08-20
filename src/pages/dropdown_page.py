from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from src.pages.base_page import BasePage

class DropdownPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dropdown"

    DROPDOWN = (By.ID, "dropdown")

    def open_page(self):
        self.open(self.URL)

    def select_option_by_value(self, value: str):
        select = Select(self.driver.find_element(*self.DROPDOWN))
        select.select_by_value(value)

    def get_selected_option(self) -> str:
        select = Select(self.driver.find_element(*self.DROPDOWN))
        return select.first_selected_option.text.strip()

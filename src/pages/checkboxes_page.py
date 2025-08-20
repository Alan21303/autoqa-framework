from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class CheckboxesPage(BasePage):
    URL = "https://the-internet.herokuapp.com/checkboxes"

    # More specific locator
    CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    def open_page(self):
        self.open(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def toggle_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        checkboxes[index].click()

    def is_checked(self, index):
        checkboxes = self.get_checkboxes()
        return checkboxes[index].is_selected()

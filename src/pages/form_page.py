# src/pages/form_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    URL = "https://formy-project.herokuapp.com/form"

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.URL)

    # Locators
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    job_title_input = (By.ID, "job-title")
    submit_button = (By.XPATH, "//a[text()='Submit']")
    success_alert = (By.CLASS_NAME, "alert")

    # Actions
    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def enter_job_title(self, job_title):
        self.driver.find_element(*self.job_title_input).send_keys(job_title)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_alert)
        ).text

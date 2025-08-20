# tests/e2e/test_form.py
import pytest
from src.pages.form_page import FormPage
from src.logger import get_logger

logger = get_logger()

@pytest.mark.e2e
def test_submit_form(driver):
    logger.info("Opening Form Page")
    page = FormPage(driver)
    page.open_page()

    logger.info("Filling the form with sample data")
    page.enter_first_name("John")
    page.enter_last_name("Doe")
    page.enter_job_title("QA Engineer")

    logger.info("Submitting the form")
    page.submit_form()

    message = page.get_success_message()
    logger.info(f"Form submission message: {message}")

    assert "success" in message.lower()

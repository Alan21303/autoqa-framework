# # tests/e2e/test_form_fail.py
# import pytest
# from src.pages.form_page import FormPage
# from src.logger import get_logger

# logger = get_logger()

# @pytest.mark.e2e
# def test_form_fail(driver):
#     logger.info("Opening Form Page with wrong URL")
    
#     # Intentionally wrong URL to trigger failure
#     page = FormPage(driver)
#     page.url = "https://formy-project.herokuapp.com/wrong_form_url"  # wrong URL
#     page.open_page()
    
#     logger.info("Submitting form (expected to fail)")
#     page.submit_form("John", "Doe", "john@example.com")

#     # This will fail and trigger screenshot
#     message = page.get_success_message()
#     logger.info(f"Form submission message: {message}")
#     assert "success" in message.lower()

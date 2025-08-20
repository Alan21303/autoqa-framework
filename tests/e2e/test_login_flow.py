import pytest
from src.pages.login_page import LoginPage

@pytest.mark.e2e
@pytest.mark.parametrize("username,password,success", [
    ("tomsmith", "SuperSecretPassword!", True),
    ("invalid_user", "invalid_pass", False),
])
def test_login_flow(driver, username, password, success):
    page = LoginPage(driver)
    page.open_page()
    page.login(username, password)

    flash_msg = page.get_flash_message()
    if success:
        assert "You logged into a secure area!" in flash_msg, f"Expected success message, got '{flash_msg}'"
    else:
        assert "Your username is invalid!" in flash_msg or "Your password is invalid!" in flash_msg, f"Expected failure message, got '{flash_msg}'"

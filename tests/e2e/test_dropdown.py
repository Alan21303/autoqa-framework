import pytest
from src.pages.dropdown_page import DropdownPage

@pytest.mark.e2e
@pytest.mark.parametrize("option_value, expected_text", [
    ("1", "Option 1"),
    ("2", "Option 2"),
])
def test_dropdown_select(driver, option_value, expected_text):
    page = DropdownPage(driver)
    page.open_page()
    page.select_option_by_value(option_value)

    selected = page.get_selected_option()
    assert selected == expected_text, f"Expected '{expected_text}', but got '{selected}'"

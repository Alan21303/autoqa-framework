import pytest
from src.pages.checkboxes_page import CheckboxesPage

@pytest.mark.smoke
def test_checkboxes_toggle(driver):
    page = CheckboxesPage(driver)
    page.open_page()

    # Initially: checkbox 0 unchecked, checkbox 1 checked
    assert not page.is_checked(0), "Checkbox 1 should start unchecked"
    assert page.is_checked(1), "Checkbox 2 should start checked"

    # Toggle both
    page.toggle_checkbox(0)
    page.toggle_checkbox(1)

    assert page.is_checked(0), "Checkbox 1 should now be checked"
    assert not page.is_checked(1), "Checkbox 2 should now be unchecked"

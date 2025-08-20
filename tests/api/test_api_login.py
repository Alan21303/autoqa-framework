# # tests/api/test_api_login.py
# import requests
# import pytest

# BASE_URL = "https://the-internet.herokuapp.com"

# @pytest.mark.api
# def test_api_login_success():
#     url = f"{BASE_URL}/login"
#     payload = {
#         "username": "tomsmith",
#         "password": "SuperSecretPassword!"
#     }
#     response = requests.post(url, data=payload)
#     assert response.status_code == 200
#     assert "secure area" in response.text.lower()

# @pytest.mark.api
# def test_api_login_failure():
#     url = f"{BASE_URL}/login"
#     payload = {
#         "username": "wronguser",
#         "password": "wrongpass"
#     }
#     response = requests.post(url, data=payload)
#     assert response.status_code == 200
#     assert "your username is invalid" in response.text.lower()

import os

import requests


class AppLibrary:
    def __init__(self):
        self._base_url = os.environ.get("APP_BASE_URL", "http://localhost:5001")

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_user(self, username, password):
        data = {
            "username": username,
            "password": password,
            "password_confirmation": password
        }

        requests.post(f"{self._base_url}/register", data=data)

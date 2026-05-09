from utils.api_client import APIClient
from utils.assertions import Assertions
from config.config import BASE_URL


class TestGetUsers:

    def test_get_all_users(self):

        response = APIClient.get(f"{BASE_URL}/users?page=2")

        Assertions.verify_status_code(response, 200)

        response_json = response.json()

        assert "data" in response_json

        
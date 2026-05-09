from utils.api_client import APIClient
from utils.assertions import Assertions
from config.config import BASE_URL


class TestSingleUser:

    def test_get_single_user(self):

        response = APIClient.get(f"{BASE_URL}/users/2")

        Assertions.verify_status_code(response, 200)

        response_json = response.json()

        assert response_json["data"]["id"] == 2


        
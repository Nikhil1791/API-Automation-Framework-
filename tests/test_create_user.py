from utils.api_client import APIClient
from utils.assertions import Assertions
from utils.json_util import JsonUtil
from config.config import BASE_URL


class TestCreateUser:

    def test_create_user(self):

        payload = JsonUtil.read_json(
            "payloads/create_user_payload.json"
        )

        response = APIClient.post(
            f"{BASE_URL}/users",
            payload
        )

        Assertions.verify_status_code(response, 201)

        response_json = response.json()

        assert response_json["name"] == "Nikhil"
        
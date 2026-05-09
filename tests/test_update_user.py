from utils.api_client import APIClient
from utils.assertions import Assertions
from utils.json_util import JsonUtil
from config.config import BASE_URL


class TestUpdateUser:

    def test_update_user(self):

        payload = JsonUtil.read_json(
            "payloads/update_user_payload.json"
        )

        response = APIClient.put(
            f"{BASE_URL}/users/2",
            payload
        )

        Assertions.verify_status_code(response, 200)

        response_json = response.json()

        assert response_json["name"] == "Nikhil Updated"

        
from utils.api_client import APIClient
from utils.assertions import Assertions
from config.config import BASE_URL


class TestDeleteUser:

    def test_delete_user(self):

        response = APIClient.delete(
            f"{BASE_URL}/users/2"
        )

        Assertions.verify_status_code(response, 204)

        
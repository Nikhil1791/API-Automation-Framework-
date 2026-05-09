import requests
from utils.logger import logger


class APIClient:

    @staticmethod
    def get(endpoint):

        logger.info(f"GET Request: {endpoint}")

        response = requests.get(endpoint)

        logger.info(f"Response Status: {response.status_code}")

        return response

    @staticmethod
    def post(endpoint, payload):

        logger.info(f"POST Request: {endpoint}")

        response = requests.post(endpoint, json=payload)

        return response

    @staticmethod
    def put(endpoint, payload):

        logger.info(f"PUT Request: {endpoint}")

        response = requests.put(endpoint, json=payload)

        return response

    @staticmethod
    def delete(endpoint):

        logger.info(f"DELETE Request: {endpoint}")

        response = requests.delete(endpoint)

        return response
    
    
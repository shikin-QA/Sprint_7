import pytest

from data.generator import generate_courier_data
from helpers.api_client import ApiClient


@pytest.fixture
def courier_data():
    return generate_courier_data()


@pytest.fixture
def created_courier(courier_data):
    ApiClient.create_courier(courier_data)
    login_response = ApiClient.login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"],
    })
    courier_id = login_response.json()["id"]

    yield courier_data, courier_id

    ApiClient.delete_courier(courier_id)
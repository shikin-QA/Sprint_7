import pytest

from data.test_data import TestData
from helpers.api_client import ApiClient


def _generate_random_string(length=10):
    import random
    import string
    return "".join(random.choices(string.ascii_lowercase, k=length))


@pytest.fixture
def courier_data():
    return {
        "login": _generate_random_string(),
        "password": _generate_random_string(),
        "firstName": _generate_random_string(),
    }


@pytest.fixture
def created_courier(courier_data):
    response = ApiClient.create_courier(courier_data)
    assert response.status_code == 201, response.text

    login_payload = {
        "login": courier_data["login"],
        "password": courier_data["password"],
    }
    login_response = ApiClient.login_courier(login_payload)
    courier_id = login_response.json()["id"]

    yield courier_data, courier_id

    ApiClient.delete_courier(courier_id)


@pytest.fixture
def courier_id_for_deletion():
    """Создаёт курьера, возвращает его id и чистит после теста."""
    login = _generate_random_string()
    password = _generate_random_string()
    firstName = _generate_random_string()

    ApiClient.create_courier({
        "login": login,
        "password": password,
        "firstName": firstName,
    })
    login_response = ApiClient.login_courier({
        "login": login,
        "password": password,
    })
    courier_id = login_response.json()["id"]

    yield courier_id

    ApiClient.delete_courier(courier_id)
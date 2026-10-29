import allure
import pytest

from data.messages import Messages
from helpers.api_client import ApiClient


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, courier_data):
        response = ApiClient.create_courier(courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        # Чистим за собой
        login_response = ApiClient.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"],
        })
        ApiClient.delete_courier(login_response.json()["id"])

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_courier_duplicate_login(self, courier_data):
        ApiClient.create_courier(courier_data)

        response = ApiClient.create_courier(courier_data)

        assert response.status_code == 409
        assert response.json()["message"] == Messages.COURIER_LOGIN_ALREADY_EXISTS

        login_response = ApiClient.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"],
        })
        ApiClient.delete_courier(login_response.json()["id"])

    @allure.title("Нельзя создать курьера без поля {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field(self, courier_data, missing_field):
        payload = courier_data.copy()
        payload.pop(missing_field)

        response = ApiClient.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.NOT_ENOUGH_CREATE_DATA
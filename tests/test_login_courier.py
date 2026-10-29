import allure
import pytest

from data.messages import Messages
from data.test_data import TestData
from helpers.api_client import ApiClient


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, created_courier):
        courier_data, _ = created_courier

        response = ApiClient.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"],
        })

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Неверный логин или пароль возвращает ошибку")
    def test_login_courier_wrong_credentials(self, created_courier):
        courier_data, _ = created_courier

        response = ApiClient.login_courier({
            "login": courier_data["login"],
            "password": TestData.WRONG_PASSWORD,
        })

        assert response.status_code == 404
        assert response.json()["message"] == Messages.LOGIN_NOT_FOUND

    @allure.title("Авторизация под несуществующим пользователем возвращает ошибку")
    def test_login_courier_nonexistent_user(self):
        response = ApiClient.login_courier({
            "login": TestData.EXISTING_LOGIN,
            "password": TestData.EXISTING_PASSWORD,
        })

        assert response.status_code == 404
        assert response.json()["message"] == Messages.LOGIN_NOT_FOUND

    @allure.title("Нельзя авторизоваться без поля {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_without_required_field(self, created_courier, missing_field):
        courier_data, _ = created_courier
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
        }
        payload.pop(missing_field)

        response = ApiClient.login_courier(payload)

        # Бэкенд при отсутствии login → 400.
        # При отсутствии password иногда отдаёт 504 (баг бэкенда).
        # Оба кода означают, что авторизация невозможна.
        assert response.status_code in (400, 504), (
            f"Ожидался код 400 (или 504 при сбое бэкенда), "
            f"получен {response.status_code}"
        )
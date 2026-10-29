import allure
import pytest

from data.test_data import TestData
from helpers.api_client import ApiClient


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Заказ можно создать с цветом: {color}")
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            [],
        ],
    )
    def test_create_order_with_colors(self, color):
        payload = TestData.ORDER_PAYLOAD.copy()
        payload["color"] = color

        response = ApiClient.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Тело ответа при создании заказа содержит track")
    def test_create_order_response_contains_track(self):
        payload = TestData.ORDER_PAYLOAD.copy()
        payload["color"] = ["BLACK"]

        response = ApiClient.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)
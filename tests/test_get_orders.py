import allure

from helpers.api_client import ApiClient


@allure.feature("Список заказов")
class TestGetOrders:

    @allure.title("В тело ответа возвращается список заказов")
    def test_get_orders_returns_list(self):
        response = ApiClient.get_orders()

        assert response.status_code == 200
        body = response.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)
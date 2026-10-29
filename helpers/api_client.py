import allure
import requests

import urls


class ApiClient:

    @staticmethod
    @allure.step("Создание курьера: POST /api/v1/courier")
    def create_courier(payload):
        return requests.post(urls.CREATE_COURIER, data=payload)

    @staticmethod
    @allure.step("Авторизация курьера: POST /api/v1/courier/login")
    def login_courier(payload):
        return requests.post(urls.LOGIN_COURIER, data=payload)

    @staticmethod
    @allure.step("Удаление курьера: DELETE /api/v1/courier/{courier_id}")
    def delete_courier(courier_id):
        return requests.delete(
            urls.DELETE_COURIER.format(courier_id=courier_id)
        )

    @staticmethod
    @allure.step("Создание заказа: POST /api/v1/orders")
    def create_order(payload):
        return requests.post(urls.CREATE_ORDER, json=payload)

    @staticmethod
    @allure.step("Получение списка заказов: GET /api/v1/orders")
    def get_orders():
        return requests.get(urls.GET_ORDERS)
import requests

import urls


class ApiClient:
    @staticmethod
    def create_courier(payload):
        return requests.post(urls.CREATE_COURIER, data=payload)

    @staticmethod
    def login_courier(payload):
        return requests.post(urls.LOGIN_COURIER, data=payload)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(urls.DELETE_COURIER.format(courier_id=courier_id))

    @staticmethod
    def create_order(payload):
        return requests.post(urls.CREATE_ORDER, json=payload)

    @staticmethod
    def get_orders():
        return requests.get(urls.GET_ORDERS)
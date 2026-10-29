class TestData:
    EXISTING_LOGIN = "nonexistent_login_12345"
    EXISTING_PASSWORD = "nonexistent_password_12345"
    WRONG_PASSWORD = "wrong_password"

    ORDER_PAYLOAD = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, ул. Ленина, 1",
        "metroStation": 1,
        "phone": "+79001234567",
        "rentTime": 3,
        "deliveryDate": "2025-12-31",
        "comment": "Тестовый заказ",
        "color": [],
    }
import requests


class PetstoreClient:
    """Клиент для взаимодействия с API Petstore."""

    def __init__(self, base_url):
        self.base_url = base_url

    def get_pet(self, pet_id):
        """Получить питомца по ID."""
        return requests.get(f'{self.base_url}/pet/{pet_id}')

    def add_pet(self, pet_data):
        """Добавить нового питомца."""
        return requests.post(f'{self.base_url}/pet', json=pet_data)

    def update_pet(self, pet_data):
        """Обновить информацию о питомце."""
        return requests.put(f'{self.base_url}/pet', json=pet_data)

    def delete_pet(self, pet_id):
        """Удалить питомца по ID."""
        return requests.delete(f'{self.base_url}/pet/{pet_id}')

    def get_order(self, order_id):
        """Получить заказ по ID."""
        return requests.get(f'{self.base_url}/store/order/{order_id}')

    def place_order(self, order_data):
        """Разместить новый заказ."""
        return requests.post(f'{self.base_url}/store/order', json=order_data)

    def delete_order(self, order_id):
        """Удалить заказ по ID."""
        return requests.delete(f'{self.base_url}/store/order/{order_id}')

    def get_user(self, username):
        """Получить пользователя по имени."""
        return requests.get(f'{self.base_url}/user/{username}')

    def create_user(self, user_data):
        """Создать нового пользователя."""
        return requests.post(f'{self.base_url}/user', json=user_data)

    def update_user(self, username, user_data):
        """Обновить информацию о пользователе."""
        return requests.put(f'{self.base_url}/user/{username}', json=user_data)

    def delete_user(self, username):
        """Удалить пользователя по имени."""
        return requests.delete(f'{self.base_url}/user/{username}')

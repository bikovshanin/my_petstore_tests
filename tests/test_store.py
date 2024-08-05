import pytest

from data.store_data import new_order
from utils.helpers import generate_random_string


@pytest.mark.usefixtures('client')
class TestOrderAPI:
    """
    Класс для тестирования API заказов в магазине.
    """

    def test_place_order(self, client):
        """
        Тестирует размещение нового заказа.
        Проверяет, что заказ успешно размещен и его данные можно получить.
        """
        response = client.place_order(new_order)
        assert (
            response.status_code == 200,
            'Failed to place order. Response: {}'.format(response.text)
        )

        response_get = client.get_order(new_order['id'])
        assert (
            response_get.status_code == 200,
            'Failed to retrieve the placed order. Response: {}'.format(
                response_get.text
            )
        )
        assert (
            response_get.json()['id'] == new_order['id'],
            'Order ID does not match.'
        )

    def test_get_order_by_id(self, client):
        """
        Тестирует получение заказа по ID.
        Проверяет, что можно получить данные заказа по его ID.
        """
        order_id = new_order['id']
        response = client.get_order(order_id)
        assert (
            response.status_code == 200,
            'Failed to get order by ID. Response: {}'.format(response.text)
        )
        assert response.json()['id'] == order_id, 'Order ID does not match.'

    def test_delete_order(self, client):
        """
        Тестирует удаление заказа.
        Проверяет, что заказ успешно удаляется и его нельзя получить.
        """
        order_id = new_order['id']
        response = client.delete_order(order_id)
        assert (
            response.status_code == 200,
            'Failed to delete order. Response: {}'.format(response.text)
        )

        response_get = client.get_order(order_id)
        assert (
            response_get.status_code == 404,
            'Deleted order should not be retrievable.'
        )

    def test_get_nonexistent_order(self, client):
        """
        Тестирует получение несуществующего заказа.
        Проверяет, что API возвращает ошибку 404 при попытке
        получить несуществующий заказ.
        """
        non_existent_id = generate_random_string()
        response = client.get_order(non_existent_id)
        assert (
            response.status_code == 404,
            'Expected 404 error for non-existent order. Response: {}'.format(
                response.text
            )
        )

    def test_place_order_with_missing_data(self, client):
        """
        Тестирует размещение заказа с отсутствующими данными.
        Проверяет, что API возвращает ошибку 400 при попытке разместить
        заказ без обязательного поля petId.
        """
        order_data = {
            'id': generate_random_string(),
            'quantity': 1,
            'status': 'placed',
            'complete': True
        }
        response = client.place_order(order_data)
        assert (
            response.status_code == 400,
            'Expected 400 error when placing order with missing data. '
            'Response: {}'.format(response.text)
        )

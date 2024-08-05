import pytest
from data.pet_data import new_pet, updated_pet
from utils.helpers import generate_random_string


@pytest.mark.usefixtures('client')
class TestPetStoreAPI:
    """
    Класс для тестирования API питомцев.
    """

    def test_add_new_pet(self, client):
        """
        Тестирует добавление нового питомца.
        Проверяет, что питомец добавлен и его данные можно получить.
        """
        response = client.add_pet(new_pet)
        assert (
            response.status_code == 200,
            'Failed to add new pet. Response: {}'.format(response.text)
        )

        response_get = client.get_pet(new_pet['id'])
        assert (
            response_get.status_code == 200,
            'Failed to retrieve the newly added pet. Response: {}'.format(
                response_get.text
            )
        )
        assert (
            response_get.json()['name'] == new_pet['name'],
            'Pet name does not match.'
        )

    def test_get_pet_by_id(self, client):
        """
        Тестирует получение питомца по ID.
        Проверяет, что можно получить данные питомца по его ID.
        """
        pet_id = new_pet['id']
        response = client.get_pet(pet_id)
        assert (
            response.status_code == 200,
            'Failed to get pet by ID. Response: {}'.format(response.text)
        )
        assert response.json()['id'] == pet_id, 'Pet ID does not match.'

    def test_update_pet_status(self, client):
        """
        Тестирует обновление статуса питомца.
        Проверяет, что статус питомца обновляется правильно.
        """
        response = client.update_pet(updated_pet)
        assert (
            response.status_code == 200,
            'Failed to update pet status. Response: {}'.format(response.text)
        )

        response_get = client.get_pet(updated_pet['id'])
        assert (
            response_get.status_code == 200,
            'Failed to retrieve updated pet. Response: {}'.format(
                response_get.text
            )
        )
        assert (
            response_get.json()['status'] == 'sold',
            'Pet status was not updated correctly.'
        )

    def test_delete_pet(self, client):
        """
        Тестирует удаление питомца.
        Проверяет, что питомец успешно удаляется и его нельзя получить.
        """
        pet_id = new_pet['id']
        response = client.delete_pet(pet_id)
        assert (
            response.status_code == 200,
            'Failed to delete pet. Response: {}'.format(response.text)
        )
        response_get = client.get_pet(pet_id)
        assert (
            response_get.status_code == 404,
            'Deleted pet should not be retrievable.'
        )


    def test_add_pet_with_missing_name(self, client):
        """
        Тестирует добавление питомца с отсутствующим именем.
        Проверяет, что API возвращает ошибку при попытке
        добавить питомца без имени.
        """
        pet_data = {
            'id': generate_random_string(),
            'photoUrls': ['http://example.com/photo2'],
            'tags': [{'id': 2, 'name': 'cat'}],
            'status': 'available'
        }
        response = client.add_pet(pet_data)
        assert (
            response.status_code == 400,
            'Expected 400 error when adding pet without a name. '
            'Response: {}'.format(response.text)
        )

    def test_get_nonexistent_pet(self, client):
        """
        Тестирует получение несуществующего питомца.
        Проверяет, что API возвращает ошибку 404
        при попытке получить несуществующего питомца.
        """
        non_existent_id = 99999
        response = client.get_pet(non_existent_id)
        assert (
            response.status_code == 404,
            'Expected 404 error for non-existent pet. Response: {}'.format(
                response.text
            )
        )

    def test_performance_get_pet(self, client):
        """
        Тестирует производительность получения питомца.
        Проверяет, что запрос на получение питомца выполняется
        за время менее 1 секунды.
        """
        pet_id = 1
        response = client.get_pet(pet_id)
        assert (
            response.status_code == 200,
            'Failed to get pet. Response: {}'.format(response.text)
        )
        assert (
            response.elapsed.total_seconds() < 1,
            'Request took too long: {} seconds'.format(
                response.elapsed.total_seconds()
            )
        )

    def test_security_sql_injection(self, client):
        """
        Тестирует защиту от SQL-инъекций.
        Проверяет, что API корректно обрабатывает потенциальную
        SQL-инъекцию в запросе.
        """
        pet_id = "1' OR '1'='1"
        response = client.get_pet(pet_id)
        assert (
            response.status_code == 400,
            'Expected 400 error for SQL injection attempt. '
            'Response: {}'.format(response.text)
        )

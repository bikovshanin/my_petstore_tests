import pytest

from data.user_data import new_user, updated_user


@pytest.mark.usefixtures('client')
class TestUserAPI:
    """
    Класс для тестирования API пользователей.
    """

    def test_create_user(self, client):
        """
        Тестирует создание нового пользователя.
        Проверяет, что пользователь успешно создан и его данные можно получить.
        """
        response = client.create_user(new_user)
        assert (
            response.status_code == 200,
            'Failed to create user. Response: {}'.format(response.text)
        )
        response_get = client.get_user(new_user['username'])
        assert (
            response_get.status_code == 200,
            'Failed to retrieve the created user. Response: {}'.format(
                response_get.text
            )
        )
        assert (
            response_get.json()['username'] == new_user['username'],
            'User username does not match.'
        )

    def test_get_user_by_username(self, client):
        """
        Тестирует получение пользователя по имени пользователя.
        Проверяет, что можно получить данные пользователя по его имени.
        """
        username = new_user['username']
        response = client.get_user(username)
        assert (
            response.status_code == 200,
            'Failed to get user by username. Response: {}'.format(
                response.text
            )
        )
        assert (
            response.json()['username'] == username,
            'User username does not match.'
        )

    def test_update_user(self, client):
        """
        Тестирует обновление пользователя.
        Проверяет, что пользователь обновлен и новые данные можно получить.
        """
        username = new_user['username']
        response = client.update_user(username, updated_user)
        assert (
            response.status_code == 200,
            'Failed to update user. Response: {}'.format(response.text)
        )

        response_get = client.get_user(username)
        assert (
            response_get.status_code == 200,
            'Failed to retrieve the updated user. Response: {}'.format(
                response_get.text
            )
        )
        assert (
            response_get.json()['email'] == updated_user['email'],
            'User email was not updated correctly.'
        )

    def test_delete_user(self, client):
        """
        Тестирует удаление пользователя.
        Проверяет, что пользователь успешно удален и его нельзя получить.
        """
        username = new_user['username']
        response = client.delete_user(username)
        assert (
            response.status_code == 200,
            'Failed to delete user. Response: {}'.format(response.text)
        )

        response_get = client.get_user(username)
        assert (
            response_get.status_code == 404,
            'Deleted user should not be retrievable.'
        )

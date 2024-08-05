# Проект автотестов для Petstore API


### Описание:

Этот проект содержит автоматические тесты для
API [Petstore](https://petstore.swagger.io/). Тесты покрывают
функциональность работы с питомцами, заказами и пользователями, обеспечивая
проверку корректности API.

### Структура проекта

```
my_petstore_tests/
├── tests/
│   ├── __init__.py
│   ├── test_pet.py
│   ├── test_store.py
│   └── test_user.py
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   └── helpers.py
├── data/
│   ├── __init__.py
│   ├── pet_data.py
│   ├── store_data.py
│   └── user_data.py
├── conftest.py
├── requirements.txt
└── pytest.ini
```

### Стек:

[![pre-commit](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3111/)
[![pre-commit](https://img.shields.io/badge/pytest-8.3-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/en/stable/)
[![pre-commit](https://img.shields.io/badge/requests-2.32-3776AB)](https://requests.readthedocs.io/en/latest/)

### Установка и запуск:

1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/bikovshanin/my_petstore_tests.git
cd petstore_tests
```

2. **Установите зависимости:** 

```bash
pip install -r requirements.txt
```

3. **Для запуска тестов используйте команду:**

```bash
pytest
```

import pytest
from utils.api_client import PetstoreClient


@pytest.fixture(scope='session')
def base_url():
    return 'https://petstore.swagger.io/v2'


@pytest.fixture(scope='session')
def client(base_url):
    return PetstoreClient(base_url)

import pytest


def pytest_addoption(parser):
    parser.addoption('--token', action='store', default='token')


@pytest.fixture
def token(request):
    return request.config.getoption('--token')

import pytest
from requests import Session

from main import headers


@pytest.fixture()
def create_session():
    session = Session()
    session.headers.update(headers)
    return session

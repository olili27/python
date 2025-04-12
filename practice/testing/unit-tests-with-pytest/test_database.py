import pytest
from database import Database

@pytest.fixture
def db():
    database = Database()
    yield database
    database.data.clear()


# db can be injected wherever the instance is needed
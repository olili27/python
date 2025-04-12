from user_manager import UserManager
import pytest


@pytest.fixture
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("tim", "tim@gmail.com") == True
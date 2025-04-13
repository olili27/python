from user_manager import UserManager
import pytest


@pytest.fixture
def user_manager():
    return UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user("tim", "tim@gmail.com") == True, 'add_user("tim", "tim@gmail.com")'


def test_get_user_when_no_user(user_manager):
    with pytest.raises(ValueError) as exec_info:
        user_manager.get_user("tim")

    assert str(exec_info.value) == "user does not exist"


def test_get_user(user_manager):
    user_manager.add_user("tim", "tim@gmail.com")
    assert user_manager.get_user("tim") == "tim@gmail.com", 'get_user("tim")'


def test_add_duplicate_user(user_manager):
    user_manager.add_user("tim", "tim@gmail.com")

    with pytest.raises(ValueError) as exec_info:
        user_manager.add_user("tim", "tim@gmail.com")

    assert str(exec_info.value) == "user already exists"

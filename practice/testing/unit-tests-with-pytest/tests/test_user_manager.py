from user_manager import UserManager
import pytest


@pytest.fixture
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("tim", "tim@gmail.com") == True, 'add_user("tim", "tim@gmail.com")'

def test_get_user(user_manager):
    assert user_manager.get_user("tim") == "tim@gmail.com", 'get_user("tim")'

# def test_add_duplicate_user(user_manager):
#     # user_manager.add_user("timo", "tim@gmail.com")
#     # with pytest.raises(ValueError, match="user already exists"):
#     #     user_manager.add_user("time", "tim@gmail.com")

#     with pytest.raises(ValueError, match="user already exists"):
#         user_manager.add_user("tim", "tim@gmail.com")

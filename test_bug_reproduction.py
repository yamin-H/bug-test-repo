import pytest
from user_manager import UserManager

def test_update_email():
    manager = UserManager()
    manager.add_user("john", "old@email.com", 25)
    manager.update_email("john", "new@email.com")
    user = manager.get_user("john")
    assert user["email"] == "new@email.com"
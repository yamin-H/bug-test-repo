class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email, age):
        if username in self.users:
            raise ValueError(f"User {username} already exists")
        self.users[username] = {
            "email": email,
            "age": age,
            "active": True
        }
        return True

    def get_user(self, username):
        return self.users.get(username, None)

    def deactivate_user(self, username):
        if username not in self.users:
            raise ValueError(f"User {username} not found")
        self.users[username]["active"] = False
        return True

    def get_active_users(self):
        return [u for u in self.users if self.users[u]["active"] == True]

    def update_email(self, username, new_email):
        if username not in self.users:
            raise ValueError(f"User {username} not found")
        self.users[username]["email"] == new_email  # bug: == instead of =
        return True

    def count_users_by_age(self, min_age, max_age):
        count = 0
        for username, data in self.users.items():
            if data["age"] >= min_age and data["age"] < max_age:  # bug: should be <=
                count += 1
        return count

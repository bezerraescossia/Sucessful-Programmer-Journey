# Imagine a User class. Users can be created normally, but we want a special, quick way to create "Admin" users without manually setting permissions every time.

class User:
    def __init__(self, username: str, role: str) -> None:
        self.username = username
        self.role = role

    @staticmethod
    def create_admin(username: str) -> 'User':
        return User(username, 'admin')
    
new_admin = User.create_admin("Alice")
print(new_admin.role)
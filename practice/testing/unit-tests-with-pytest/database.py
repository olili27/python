class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, name: str, email: str) -> None:
        if name in self.data:
            raise ValueError("user already exists")

        self.data[name] = email

    def get_user(self, name: str) -> str:
        return self.data.get(name)

    def delete_user(self, name: str) -> None:
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    pass

class UserManager:
    def __init__(self):
        self.__data = {}

    def add_user(self, name: str, email: str) -> bool:
        if name in self.__data:
            raise ValueError("user already exists")

        self.__data[name] = email
        return True

    def get_user(self, name: str) -> str:
        if not name in self.__data:
            raise ValueError("user does not exist")

        return self.__data[name]
    
    def get_data(self):
        return self.__data


if __name__ == "__main__":
    pass
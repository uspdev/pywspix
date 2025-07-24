class Headers:
    def __init__(self, user, password):
        self.__user = user
        self.__password = password

    def generate(self):
        header_content = {
            "X-Username": self.__user,
            "X-Password": self.__password
        }
        return header_content
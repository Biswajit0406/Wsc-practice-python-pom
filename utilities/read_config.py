from configparser import RawConfigParser

biswa = RawConfigParser()
biswa.read("C:/Users/KIIT/PycharmProjects/pythonProject1/configurations/config.ini")

class Read_Config:
    @staticmethod
    def get_url():
        url = biswa.get('admin','url')
        return url
    @staticmethod
    def get_username():
        username = biswa.get('admin','username')
        return username
    @staticmethod
    def get_password():
        password = biswa.get('admin','password')
        return password




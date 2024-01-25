import random
from getpass import getpass

class Account:
    def __init__(self, username, password, deposit) -> None:
        self.__UID = random.randint(8000_000_000, 8999_999_999)
        self.__username = username
        self.__password = self.__encrypt(password)
        self.__deposit  = deposit

    def __encrypt(self, password):
        return hash(password)
    
    def __showInfo(self):
        UID      = f'UID      : {self.__UID}\n'
        username = f'User Name: {self.__username}\n'
        deposit  = f'Deposit  : {self.__deposit} NTD'
        return UID + username + deposit

    def authenticate(self, username, password):
        if username != self.__username or self.__encrypt(password) != self.__password:
            print('Wrong username or password, access denied')
        else:
            print('Access Granted')
            print(self.__showInfo())

a1 = Account('Kenny', '12345678', 12000)

username = input('Username: ')
password = getpass('Password:')
a1.authenticate(username, password)
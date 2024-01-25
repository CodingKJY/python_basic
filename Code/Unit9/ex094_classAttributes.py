class Account:
    number_of_accounts = 0

    def __new__(cls, username):
        cls.number_of_accounts += 1
        return super().__new__(cls)

    def __init__(self, username) -> None:
        self.username = username
    
a1 = Account('Neil')
a2 = Account('Jim')
a3 = Account('Kely')

print(a1.number_of_accounts)
print(a2.number_of_accounts)
print(a3.number_of_accounts)

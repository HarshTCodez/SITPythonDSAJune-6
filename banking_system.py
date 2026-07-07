class Account:
    __account_number: str
    __name: str

    @staticmethod
    def validate_account_number(account_number: str):
        if type(account_number) != str:
            raise ValueError("Account Number should be a string")
        for char in account_number:
            if not char.isdigit():
                raise ValueError("Only Digits are allowed")

    @staticmethod
    def validate_name(name):
        if type(name) != str:
            raise ValueError("Account Name should be a string")
        for char in name:
            if char == " ":
                continue
            if not char.isalpha():
                raise ValueError("Only Alphabets are allowed")

    def __set_account_number(self, val):
        Account.validate_account_number(val)
        self.__account_number = val

    def __init__(self, account_number, name):
        self.__set_account_number(account_number)
        self.name = name

    @property
    def account_number(self):
        return self.__account_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        Account.validate_name(val)
        self.__name = val


acc1 = Account("1234", "Anmol Jhamb")
print(acc1)
print(acc1.account_number)
print(acc1.name)

# acc1.__set_account_number(123) # will not work!!

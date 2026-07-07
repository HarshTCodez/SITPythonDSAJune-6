class Account:
    PIN_LENGTH = 4

    __account_number: str
    __name: str
    __pin: str

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

    @staticmethod
    def validate_pin(val):
        if type(val) != str:
            raise ValueError("Pin should be a string")
        for char in val:
            if not char.isdigit():
                raise ValueError("Only Digits are allowed")
        if len(val) != Account.PIN_LENGTH:
            raise ValueError(f"The pin should be {Account.PIN_LENGTH} digits.")

    def __set_account_number(self, val):
        Account.validate_account_number(val)
        self.__account_number = val

    def __set_pin(self, val):
        Account.validate_pin(val)
        self.__pin = val

    def __init__(self, account_number, name, pin):
        self.__set_account_number(account_number)
        self.__set_pin(pin)
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

    def verify_pin(self, password):
        if password == self.__pin:
            return True
        return False


acc1 = Account(
    "1234",
    "Anmol Jhamb",
    "1234",
)
print(acc1)
print(acc1.account_number)
print(acc1.name)

# acc1.__set_account_number(123) # will not work!!

print(acc1.verify_pin("1234"))

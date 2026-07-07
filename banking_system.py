class Account:
    PIN_LENGTH = 4
    BANK_NAME = "Kotak Bank"

    __account_number: str
    __name: str
    __pin: str
    __balance: int
    __transactions: list

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

    @staticmethod
    def validate_amount(val):
        if type(val) != int:
            raise ValueError("Amount can only be a number")
        if val < 0:
            raise ValueError("Amount can only be positive")

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
        self.__balance = 0
        self.__transactions = []

    @property
    def account_number(self):
        return self.__account_number

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    @name.setter
    def name(self, val):
        Account.validate_name(val)
        self.__name = val

    @property
    def transcations(self):
        return self.__transactions

    def verify_pin(self, password):
        if password == self.__pin:
            return True
        return False

    def add_deposit(self, amount):
        Account.validate_amount(amount)
        self.__balance += amount
        self.__transactions.append((amount, "CREDIT"))

    def withdraw(self, pin, amount):
        if not self.verify_pin(pin):
            raise ValueError("Wrong Pin")
        Account.validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Account doesn't have that much money.")
        self.__balance -= amount
        self.__transactions.append((amount, "DEBIT"))


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
print(acc1.balance)
acc1.add_deposit(100_000)
print(acc1.balance)
acc1.withdraw("1234", 12000)
print(acc1.balance)
print(acc1.transcations)

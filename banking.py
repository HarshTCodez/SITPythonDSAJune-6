from random import randint

from banking_system import Account

accounts: dict[str, Account] = {}


def get_random_number():
    return str(randint(1000, 9999))


def open_new_account():
    try:
        account_number = get_random_number()
        account_name = input("Enter your name: ")
        pin = input("Enter your pin: ")
        new_account = Account(account_number, account_name, pin)
        print(
            f"Congratulations, you've opened an account at the {Account.BANK_NAME}.\nYour account number is {new_account.account_number}"
        )
        accounts[account_number] = new_account
    except ValueError as e:
        print(e)


def login_in_existing_account():
    account_number = input("Enter your account number: ")
    account_pin = input("Enter your account pin: ")
    if account_number not in accounts:
        print("We cannot find your account number, please check.")
        return
    current_account = accounts[account_number]
    if not current_account.verify_pin(account_pin):
        print("Your pin is wrong")
        return
    print("You've successfully logged in!")

    while True:
        print("Enter 1 to view your balance")
        print("Enter 2 to deposit")
        print("Enter 3 to withdraw")
        print("Enter 4 to view transcations")
        print("Enter 5 to change your pin")
        print("Enter 6 to view account details")
        print("Enter 7 to change your account name")
        print("Enter 9 to logout")
        choice = input("What do you want to do?\nEnter Choice: ")
        if choice == "1":
            print(f"Your current balance is: {current_account.balance}")
        if choice == "2":
            try:
                amount = input("Enter the amount you wish to deposit?\nAmount:")
                current_account.add_deposit(int(amount))
            except ValueError as e:
                print(e)
        if choice == "3":
            try:
                amount = input("Enter the amount you wish to deposit?\nAmount:")
                current_account.withdraw(account_pin, int(amount))
            except ValueError as e:
                print(e)
        if choice == "4":
            print(current_account.transcations)
        if choice == "5":
            new_pin = input("Enter new pin: ")
            current_account.change_pin(account_pin, new_pin)
        if choice == "6":
            print(current_account)
        if choice == "7":
            new_name = input("Enter New Name: ")
            current_account.name = new_name
        if choice == "9":
            return


def main():
    while True:
        print("Enter 1 for opening a new account")
        print("Enter 2, if you already have an account")
        print("Enter 3, if you want to exit")
        choice = input("What do you want to do?\nEnter Choice: ")
        if choice == "3":
            print("Closing the application")
            exit()
        if choice == "1":
            open_new_account()
        if choice == "2":
            login_in_existing_account()


if __name__ == "__main__":
    main()

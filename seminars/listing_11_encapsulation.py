"""
Programming 2026.

Seminar 10.

Encapsulation.
"""

# pylint:disable=too-few-public-methods


class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def update_balance(self, amount):
        self.__balance += amount
    def validate_transaction(self, amount):
        if type(amount) in (int, float) and amount > 0:
            return True
        return False
    def deposit(self, amount):
        if self.validate_transaction(amount):
            self.update_balance(amount)
            print(f'Счет пополнен на {amount}. Текущий баланс: {self.__balance}')
        else:
            print("Error")
    def withdraw(self, amount):
        if not self.validate_transaction(amount):
            print('Ошибка. Сумма должна быть больше нуля')
            return
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'Снято {amount}. Остаток: {self.__balance}')
        else:
            print('Недостаточно средств')

    """
    Represents a bank account.

    Instance attributes:
        owner (str): The owner of the account.
        balance (float): The current balance of the account.

    Instance methods:
        deposit(amount: float) -> None:
            Adds money to the account.
        withdraw(amount: float) -> None:
            Subtracts money from the account if sufficient funds exist.
        get_balance() -> float:
            Returns the current balance of the account.
        update_balance(amount: float) -> None:
            Updates the balance.
        validate_transaction(amount: float) -> bool:
            Checks if a transaction amount is valid.
    """


class Bank:
    def __init__(self, name, accounts, next_account_number):
        self.name = name
        self.accounts = {}
        self.next_account_number = 1000
    def generate_account_number(self):
        current_number = self.generate_account_number
        self.next_account_number += 1
        return current_number
    def create_account(self, owner_name):
        acc_num = self.generate_account_number()
        new_account = BankAccount(owner_name)
        self.accounts[acc_num] = new_account
        print(f'Создан счет {acc_num} для {owner_name}')
        return new_account
    def deposit_to_account(self, account_number, amount):
        if account_number in self.accounts:

    """
    Represents a bank that manages accounts and provides financial services.

    Instance attributes:
        name (str): The name of the bank.
        accounts (dict): A dictionary with BankAccount objects.
        next_account_number (int): The next account number to be assigned.

    Instance methods:
        create_account(owner_name: str) -> BankAccount:
            Creates a new bank account for a person.
        deposit_to_account(account_number: int, amount: float) -> None:
            Deposits money into a specific account.
        provide_loan(account_number: int, amount: float) -> None:
            Provides a loan to a specific account.
        get_account_balance(account_number: int) -> float:
            Returns the balance of a specific account.
        generate_account_number() -> int:
            Generates a new account number.
    """


class Person:
    """
    Represents a person who can perform financial transactions through their bank account.

    Instance attributes:
        name (str): The name of the person.
        account (BankAccount): The person's bank account object.

    Instance methods:
        make_purchase(amount: float) -> None:
            Subtracts money from the person's account for a purchase.
        transfer_money(recipient: Person, amount: float) -> None:
            Transfers money from this person's account to another person's account.
        add_funds(amount: float) -> None:
            Adds money to the person's account.
    """


def main() -> None:
    """
    Launch listing.
    """
    # Work here
    print("Created classes")


if __name__ == "__main__":
    main()

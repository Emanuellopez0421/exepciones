class BankAccount:
    def __init__(self, holder: str, balance: float = 0.0):
        self.__holder = holder
        self.__balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            print("Error: Cannot deposit a negative or zero amount.")
        else:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Error: Cannot withdraw a negative or zero amount.")
        elif amount > self.__balance:
            print("Error: Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")

    def check_balance(self) -> float:
        return self.__balance

    def check_holder(self) -> str:
        return self.__holder

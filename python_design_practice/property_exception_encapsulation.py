# banking system using decorator setter, getter exception handling 

class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, account_number, account_holder, balance):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_holder(self):
        return self._account_holder

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = new_balance

class Bank:
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Transaction error: Invalid deposit amount.")
            self.account.balance += amount
            print(f"Deposited {amount} to the account successfully.")
        except InvalidAmountError as e:
            print(str(e))

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Transaction error: Invalid withdrawal amount.")
            if self.account.balance < amount:
                raise InsufficientFundsError("Sorry you have insufficient funds.")
            self.account.balance -= amount
            print(f"Withdrawn {amount} from the account successfully.")
        except InvalidAmountError as e:
            print(str(e))
        except InsufficientFundsError as e:
            print(str(e))

    def main(self):
        print("*" * 98)
        print("\t\t\t\t\tBanking System")
        print("*" * 98)

        print(f"\nAccount number: {self.account.account_number}")
        print(f"Account holder: {self.account.account_holder}\n")

        print("Transactions:")
        self.deposit(100.0)
        # Invalid amount
        self.deposit(-50.0)

        self.withdraw(300.0)
        # Insufficient funds
        self.withdraw(100000.0)

        print(f"\nYour current balance is: {self.account.balance}")

if __name__ == "__main__":
    account = Account("118539001006040", "Steve Daniel", 50000.0)
    bank = Bank(account)
    bank.main()
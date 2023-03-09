# imports necessary classes from each file
from Account_Final import Account
"""
Bank class

Creates an empty list to represent the bank and stores methods for adding to the bank, removing from the bank,
finding accounts in the bank, and adding monthly interest to all accounts.
"""
class Bank():
    # Defines the maximum accounts in the bank as 100
    max_accounts = 100
    """
    Constructor method

    Creates a variable attribute to represent the bank.
    """
    def __init__(self):
        # An empty list to represent the bank
        self.accounts = []
    """
    addAccountToBank method

    If the bank has less than 100 accounts the new account will be addded.
    """
    def addAccountToBank(self, account):
        if len(self.accounts) < self.max_accounts:
            # Adds the account to the next open index in the bank
            self.accounts.append(account)
            return True
        else:
            # If full this print statement is returned
            print("No more accounts available")
            return False
    """
    removeAccountToBank method

    Iterates through the bank to find the account and removes it.
    """
    def removeAccountFromBank(self, account):
        if account in self.accounts:
            # Finds selected account in bank and removes it.
            self.accounts.remove(account)
            return True
        else:
            return False
    """
    findAccount method

    Iterates through the bank then to find the account and returns it.
    """
    def findAccount(self, account_number):
        for account in self.accounts:
            # Finds account in bank with matching account number.
            if account.get_account_number() == account_number:
                return account
        return None
    """
    addMonthlyInterest method

    Iterates through the bank and adds the inputted interest to all accounts.
    """
    def addMonthlyInterest(self, percent):
        # Set yearly interest rate then divide by 12 to get monthly interest
        monthlyInterestRate = percent / 12 
        for account in self.accounts:
            if account is not None:
                balance = account.get_balance()
                interest = balance * monthlyInterestRate
                # Deposits the interest based on the calculation with the accounts balance.
                account.deposit(interest)
        print(f"The monthly interest rate is now {monthlyInterestRate:.2f} %")


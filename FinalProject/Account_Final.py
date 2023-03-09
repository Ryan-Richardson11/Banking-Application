# imports random module as well as necessary classes from each file
import random
from BankUtility_Final import BankUtility
"""
Account class

Stores the methods related to account information and updating balances.
"""
class Account():
    """
    Constructor method

    Creates variable attributes for the account owner's first name, last name, ssn, pin, and account number.
    """
    def __init__(self, owner_first_name, owner_last_name, ssn, pin):

        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.ssn = ssn
        self.balance = 0.00
        self.account_number = None
        self.pin = pin
    """
    generate_pin method

    Static method that is called in BankManager class to create a random pin.
    """
    @staticmethod
    def generate_pin():
        return str(random.randint(1000, 9999))
    """
    set_owener_first_name method

    Sets the owner's first name to be called.
    """
    def set_owner_first_name(self, owner_first_name):
        self.owner_first_name = owner_first_name
    """
    get_owener_first_name method

    Gets the owner's first name to be called in a string.
    """
    def get_owner_first_name(self):
        return self.owner_first_name
    """
    set_owener_last_name method

    Sets the owner's last name to be called.
    """
    def set_owner_last_name(self, owner_last_name):
        self.owner_last_name = owner_last_name
    """
    get_owener_last_name method

    Gets the owner's last name to be called in a string.
    """
    def get_owner_last_name(self):
        return self.owner_last_name
    """
    set_ssn method

    Sets the ssn to be called.
    """
    def set_ssn(self, ssn):
        self.ssn = ssn
    """
    get_ssn method

    Gets the ssn to be called in a string.
    """
    def get_ssn(self):
        return self.ssn
    """
    set_account_number method

    Uses a function from BankUtility class to create a random account number.
    """
    def set_account_number(self):
        self.account_number = BankUtility.generateRandomInteger(10000000, 99999999)
    """
    get_account_number method

    returns the account number.
    """
    def get_account_number(self):
        return self.account_number
    """
    set_pin method

    Called when changing pins in the BankManager class to set the new pin.
    """
    def set_pin(self, new_pin):
        self.pin = new_pin
    """
    get_pin method

    Returns the new pin.
    """
    def get_pin(self):
        return self.pin
    """
    set_balance method

    Sets the starting balance for the account which should be zero.
    """
    def set_balance(self, balance):
        self.balance = balance
    """
    get_balance method

    Returns the balance whenever altered in the BankManager Class.
    """
    def get_balance(self):
        return round(self.balance, 2)
    """
    deposit method

    Adds the inputted amount to the accounts balance.
    """
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            return None
    """
    withdraw method

    Subtracts the withdrawn amount from the account balance.
    """
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Your withdrawal was successfull!")
            return self.balance    
        else:
            print("Error: Insufficient funds")
            return None
    """
    ATM_withdraw method

    Subtracts the withdrawn amount from the account balance. Only Accessible in multiples of 5 and cannot exceed 1000.
    Number of 20, 10, and 5 dollar bills will be printed as well.
    """
    def ATM_withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            # Calculates number of 20, 10, and 5 dollar bills that will be dispensed.
            if amount // 20 >= 1:
                num_20 = amount // 20
                print(f"Number of 20 dollar bills: {num_20:.0f}")
                amount = amount % 20
            if amount // 10 >= 1:
                num_10 = amount // 10
                print(f"Number of 10 dollar bills: {num_10:.0f}")
                amount = amount % 10
            if amount // 5 >= 1:
                num_5 = amount // 5
                print(f"Number of 5 dollar bills: {num_5:.0f}")
        else:
            print("Error: Insufficient funds")
    """
    is_valid_pin method

    Checks that the pin is 4 characters, all digits, and is equal to the inputted pin.
    """
    def is_valid_pin(self, pin):
        if (len(pin) == 4 and pin.isdigit() and  pin == self.pin):
            return True
        else:
            return False
    """
    is_valid_ssn method

    Checks that the SSN is 9 characters and all digits.
    """
    def is_valid_ssn(self, ssn):
        try:
            if len(ssn) != 9:
                print("Invalid SSN: must be 9 digits\n")
                return False
            if not ssn.isdigit():
                print("Invalid SSN: must only contain digits\n")
                return False
            return True
        except: ValueError
    """
    __str__ method

    Returns a formatted string with all of the accounts information.
    """
    def __str__(self):
        string = f"""
        Account Number: {self.account_number}
        Owner First Name: {self.owner_first_name}
        Owner Last Name: {self.owner_last_name}
        Owner SSN: {self.ssn} 
        PIN: {self.pin} 
        Balance: ${self.balance:.2f}\n"""
        return string


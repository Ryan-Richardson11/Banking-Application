# imports random module
import random
"""
BankUtility class

Creates an empty list to represent the bank and stores methods for adding to the bank, removing from the bank,
finding accounts in the bank, and adding monthly interest to all accounts.
"""
class BankUtility:
    """
    Constructor method

    No variables are created. Passed for future uses.
    """
    def __init__(self):
        pass
    """
    promptUserForString method

    A static method used to test the SSN input as a string in the BankManager class and if it is numeric.
    """    
    @staticmethod
    def promptUserForString(prompt):
        try:
            user_input = input(prompt)
            # Makes sure the user input is numeric.
            if BankUtility.isNumeric(user_input):
                return user_input
        except: ValueError
        print("That input is invald\n")
    """
    promptUserForPositiveNumber method

    A static method for all the monetary inputs in the BankManager class to make sure they are all positive numbers.
    """    
    @staticmethod
    def promptUserForPositiveNumber(prompt):
        while True:
            user_input = input(prompt)
            # Makes sure the input is numeric and greater than zero.
            if BankUtility.isNumeric(user_input):
                number = float(user_input)
                if number < 0:
                    print("Input cannot be negative. Try again.")
                else:
                    return number
            else:
                print("Input is not a number. Try again.")
    """
    generateRandomInteger method

    A static method used to generate the account number for all accounts.
    """
    @staticmethod
    def generateRandomInteger(min_val, max_val):
        # Returns number between the defined min and max values.
        return random.randint(min_val, max_val)
    """
    convertFromDollarsToCents method

    A static method that takes the balance as dollars and cents and returns the value in cents only.
    """
    @staticmethod
    def convertFromDollarsToCents(amount):
        if amount > 0:
            # Takes the accounts balance and converts it to cents with this formula.
            convert_to_cents = int(amount * 100)
            print(f"Your balance is {convert_to_cents} cents\n")
            return int(convert_to_cents)
        else:
            return None
    """
    isNumeric method

    A static method that checks if the input is only digits.
    """
    @staticmethod
    def isNumeric(choice):
        # Checks that the input is numeric.
        return all(c.isdigit() or c == '-' for c in choice)

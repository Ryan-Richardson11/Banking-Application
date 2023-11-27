Mock Banking System
- This project implements a simple bank system in Python, featuring account management, transactions, and banking operations. The system comprises several files, each serving a specific purpose.

Account_Final.py
Overview
- This file defines the Account class, responsible for managing account information and transactions.

Class Methods
- Constructor (__init__):

- Initializes account details such as owner's name, SSN, balance, account number, and PIN.
- generate_pin (Static Method):

- Generates a random PIN for an account.
- Balance-Related Methods:

- set_balance, get_balance, deposit, withdraw, ATM_withdraw: Manage the account balance.
Owner Information Methods:

- set_owner_first_name, get_owner_first_name, set_owner_last_name, get_owner_last_name, set_ssn, get_ssn: Manage owner information.
Account Number and PIN Methods:

- set_account_number, get_account_number, set_pin, get_pin: Manage account number and PIN.
Validation Methods:

- is_valid_pin, is_valid_ssn: Validate PIN and SSN.
String Representation Method (__str__):

- Provides a formatted string containing account information.

CoinCollector_Final.py
Overview
- This file defines the CoinCollector class, which creates a dictionary of coins with associated values and includes a method to parse coins.

Class Methods
parseChange:
- Iterates through inputted coins, assigns their values based on the dictionary, and returns the sum of their values.
Parameters:
- coins: A string containing coin abbreviations (e.g., 'PDQ' for Penny, Dime, Quarter).
Returns:
- The total sum of the coin values.

BankManager_Final.py
Overview
This file defines the BankManager class, which acts as the interface for interacting with the bank system.

Class Methods
- Constructor (__init__):

- Initializes an instance of the bank.
- promptForAccountNumberAndPIN:

- Asks the user for their account number and PIN, validating the input.
main:

- Handles user interactions and executes various banking operations based on user input.
BankUtility_Final.py
Overview
- This file defines the BankUtility class, providing utility methods used across the bank system.

Class Methods
Static Methods:
- promptUserForString: Ensures valid SSN input.
- promptUserForPositiveNumber: Ensures positive numeric inputs.
- generateRandomInteger: Generates a random integer for account numbers.
- convertFromDollarsToCents: Converts the account balance to cents.
- isNumeric: Checks if input is numeric.
- ank_Final.py
Overview
- This file defines the Bank class, representing the bank and managing accounts.

Class Methods
- Constructor (__init__):

- Initializes an empty list to represent the bank.
Bank Operation Methods:

- addAccountToBank, removeAccountFromBank, findAccount: Manage accounts in the bank.
- addMonthlyInterest: Adds monthly interest to all accounts in the bank.
How to Use
- Run BankManager_Final.py:

- Execute this file to interact with the bank system.
- Follow the prompts to perform various banking operations.

Unittesting for different scenarios:
- UnitTestsFinal.py

# imports necessary classes from each file
from Account_Final import Account
from Bank_Final import Bank
from BankUtility_Final import BankUtility
from CoinCollector_Final import CoinCollector
"""
BankManager class

Stores the testing methods for parsing change, raising value error, and an empty list.
"""
class BankManager():
    """
    Constructor method

    Creates an instance of the bank.
    """
    def __init__(self):
        self.bank = Bank()
    """
    promptForAccountNumberAndPIN method

    Asks for the users account number and pin both are valid it will return the account.
    """
    def promptForAccountNumberAndPIN(self):
        account_number = int(input("Please enter your account number: "))
        account = self.bank.findAccount(account_number)
        # Iterates through accounts in the bank and searches for a valid account number and pin.
        if account == None:
            print(f"Account not found for account number: {account_number} \n")
            return None
        else:
            pin = input("Please enter your PIN: ")
            if account.is_valid_pin(pin):
                return account
            else:
                print("Invalid PIN \n")
                return None
    """
    main method

    Executes all tasks related to the bank.
    """
    def main(self):
        """
        While statement

        Prints a list of options and prompts for the users input. Based on the choice one of the options will be executed.
        """
        while True:
            print("===============================================")
            print("1. Open an Account")
            print("2. Get Account information and balance")
            print("3. Change PIN")
            print("4. Deposit money in account")
            print("5. Transfer money between accounts")
            print("6. Withdraw money from account")
            print("7. ATM withdrawal")
            print("8. Deposit Change")
            print("9. Close an account")
            print("10. Add monthly interest to all accounts")
            print("11. Display balance in cents")
            print("12. End Program")
            print("===============================================")
            # User enters their input choice here.
            choice = input("Enter your choice (1-11): ")
            # Open Account: Asks the user for details and creates and account object in the bank.
            if choice == "1":
                owner_first_name = str(input("Enter Account Owner's First Name: "))
                owner_last_name = str(input("Enter Account Owner's Last Name: "))
                ssn = BankUtility.promptUserForString("Enter Account Owner's SSN (9 digits no '-'): ")
                pin = Account.generate_pin()
                # Creates an account object in the bank using the above information.
                new_account = Account(owner_first_name, owner_last_name, ssn, pin)
                if not new_account.is_valid_ssn(ssn):
                    continue
                new_account.set_account_number()
                # Adds the new account to the bank
                self.bank.addAccountToBank(new_account)
                print(new_account.__str__())
                print("You have successfully opened an account!\n")
            # Get account information and balance: Prompts for account number and pin and displays account information.
            elif choice == "2":
                account = self.promptForAccountNumberAndPIN()
                if account is not None:
                    print("Here is the account's information")
                    print(account.__str__())
            # Change PIN: Prompts for account number and pin and takes and sets a new pin for the account.
            elif choice == "3":
                account = self.promptForAccountNumberAndPIN()
                if account is not None:
                    # If the old pin is valid, move forward to change pins
                    old_pin = input("Enter old PIN: ")
                    if not account.is_valid_pin(old_pin):
                        print("Invalid old PIN \n")
                    else:
                        new_pin = input("Enter new PIN: ")
                        confirm_pin = input("Enter new PIN again to confirm: ")
                        # Ensures both pins entered match
                        if new_pin == confirm_pin:
                            account.set_pin(new_pin)
                            if account.is_valid_pin(new_pin):
                                print("PIN updated\n")
            # Deposit Money in account: Prompts for account number and pin then asks for an input and adds that to the account balance.
            elif choice == "4":
                account = self.promptForAccountNumberAndPIN()
                if account is not None:
                    amount = BankUtility.promptUserForPositiveNumber("Enter amount to deposit in dollars and cents (e.g. 2.57): ")
                    # Adds the entered amount to the bank account from the deposit method in the Account class.
                    account.deposit(amount)
                    print("Your deposit was successfull!")
                    print(f"Your updated balance is ${account.get_balance():.2f}\n")
            # Transfers money between accounts: Prompts for account number and pin for a transfer from and transfer to account then asks for an input.
            elif choice == "5":
                print("Transfer From")
                account = self.promptForAccountNumberAndPIN()
                if account is not None:
                    amount = BankUtility.promptUserForPositiveNumber("Enter amount to transfer in dollars and cents (e.g. 2.57): ")
                    # Input is widrawn from the Transfer from account.
                    account.withdraw(amount)
                print("Transfer To")
                account = self.promptForAccountNumberAndPIN()
                # Input is deposited in the transfer to account.
                account.deposit(amount)
                print("Your transfer was successful!\n")
            # Withdraw money from account: Prompts for account number and pin then asks for an input and subtracks that from the account balance.
            elif choice == "6":
                account = self.promptForAccountNumberAndPIN()
                if account is not None:
                    amount = BankUtility.promptUserForPositiveNumber("Enter amount to withdraw in dollars and cents (e.g. 2.57): ")
                    # Subtracts the entered amount from the bank account with the withdraw method in the Account class.
                    account.withdraw(amount)
                    print(f"Your updated balance is ${account.get_balance():.2f}\n")
            # ATM withdrawal: Prompts for account number and pin then asks for an input and subtracks that from the account balance. 
            elif choice == "7":
                account = self.promptForAccountNumberAndPIN()
                if account is not None:
                    amount = BankUtility.promptUserForPositiveNumber("Enter the amount to withdraw (in multiples of $5): ")
                    try:
                        # Amount must be 5 or greater and 1000 to be valid
                        amount = float(amount)
                        if amount < 5 or amount > 1000 or amount % 5 != 0:
                            print("Invalid amount. Try again.\n")
                        else:
                            # Function call will print number of 20's, 10's, and 5's dipensed.
                            account.ATM_withdraw(amount)
                            print(f"Your updated balance is ${account.get_balance():.2f}\n")
                    except ValueError:
                        print("Invalid amount. Try again.\n")
            # Deposit Change: Prompts for account number and pin then asks for an input as a string, converts in into a float, and adds it to the account balance.
            elif choice == "8":
                account = self.promptForAccountNumberAndPIN()
                if account is not None:
                    # Creates an instance of the CoinCollector class.
                    coin_collector = CoinCollector()
                    change_deposit = input("Enter the coins you want to deposit: ")
                    # Counts the change based on the key values and by calling parseChange from the CoinCollector class.
                    deposit_count = coin_collector.parseChange(change_deposit)
                    account.deposit(deposit_count)
                    print(f"You have deposited ${deposit_count:.2f} in coins to your account.\n")
                    print(f"Your updated balance is ${account.get_balance():.2f}\n")
            # Close an account: Prompts for account number and pin then removes that account object from the bank.
            elif choice == "9":
                account = self.promptForAccountNumberAndPIN()
                if account is not None:
                    # If the account is in the bank it will be removed.
                    self.bank.removeAccountFromBank(account)
                    print("Your account has been closed.\n")
            # Add monthly interest to all accounts: Prompts for the yearly interest then prints out what the monthly interest will be.
            elif choice == "10":
                if len(self.bank.accounts) == 0:
                    print("There are no accounts to add interest to.\n")
                else:
                    for account in self.bank.accounts:
                            percent = BankUtility.promptUserForPositiveNumber("Enter the yearly interst rate (%): ")
                            # Adds monthly interest to all accounts based on the percentage entered.
                            self.bank.addMonthlyInterest(percent)
                            print("Monthly interest has been added to all accounts.\n")
            # Display balance in cents: Prompts for account number and pin then converts the account balance to cents.
            elif choice == "11":
                account = self.promptForAccountNumberAndPIN()
                if account is not None:
                    BankUtility.convertFromDollarsToCents(account.get_balance())
            # End Program: breaks the loop and exits the program.
            elif choice == "12":
                break
            # Invalid choice: All inputs that are not 1-12 will be an invalid choice.
            else:
                print("Invalid choice \n")
                continue

# Creates an instance of the Bank manager class and calls main
Manager = BankManager()
Manager.main()

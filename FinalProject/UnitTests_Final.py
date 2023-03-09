# imports unittest as well as the classes from each file
import unittest
from CoinCollector_Final import CoinCollector
from Account_Final import Account
from Bank_Final import Bank
from BankUtility_Final import BankUtility
"""
TestCoinCollector class

Stores the testing methods for parsing change, raising value error, and an empty list.
"""
class TestCoinCollector(unittest.TestCase):
    """
    test_parseChange_with_valid_coins method

    Presents valid coins and checks if it correctly evaluates the outcome of them.
    """
    def test_parseChange_with_valid_coins(self):
        collector = CoinCollector()
        coins = ['P', 'N', 'D', 'Q', 'H', 'W']
        expected_total_cents = 1.91
        total_cents = collector.parseChange(coins)
        self.assertAlmostEqual(total_cents, expected_total_cents, places=2)
    """
    test_parseChange_with_invalid_coin method

    Presents an invalid coin (Z) and checks if it correctly raises a ValueError.
    """
    def test_parseChange_with_invalid_coin(self):
        collector = CoinCollector()
        coins = ['P', 'N', 'D', 'Z']
        expected_total_cents = 0.16
        with self.assertRaises(ValueError):
            collector.parseChange(coins)
    """
    test_parseChange_with_empty_list method

    Presents no input and sees if it is calculated to be zero.
    """
    def test_parseChange_with_empty_list(self):
        collector = CoinCollector()
        coins = []
        expected_total_cents = 0
        total_cents = collector.parseChange(coins)
        self.assertEqual(total_cents, expected_total_cents)
"""
TestAccount class

Stores setup and testing methods for deposit, withdraw, and is_valid_pin.
"""
class TestAccount(unittest.TestCase):
    """
    setUp method

    creates an account objects for the other methods to test against.
    """
    def setUp(self):
        self.account = Account("Ryan", "Richardson", "123456789", "1234")
    """
    test_deposit method

    Attempts to deposit an amount then sees if the accounts balance is that amount.
    """
    def test_deposit(self):
        #Deposits into bank and checks balance for that deposit
        self.account.deposit(500.00)
        self.assertEqual(self.account.get_balance(), 500.00)
    """
    test_negative_deposit method

    Attempts to deposit an amount that is negative and should return none.
    """
    def test_negative_deposit(self):
        self.account.deposit(-500.00)
        self.assertIsNone(self.account.deposit(-500.00))  
    """
    test_withdraw method

    Sets a balance then tries to withdraw an amount and sees if the new balance is correct.
    """
    def test_withdraw(self):
        # Withdraw a an amount under the balance
        self.account.set_balance(500.00)
        self.account.withdraw(100.00)
        self.assertEqual(self.account.get_balance(), 400.00)
    """
    test_withdraw_overdraft method

    Tries to withdraw an amount greater than the balance and should return None.
    """
    def test_withdraw_overdraft(self):
        #Withdraw an amount larger than balance
        self.account.withdraw(600.00)
        self.assertIsNone(self.account.withdraw(600.00))
    """
    test_is_valid_pin method

    Checks that the pin matches the account and returns True.
    """
    def test_is_valid_pin(self):
        #Checks for a valid PIN
        self.assertTrue(self.account.is_valid_pin("1234"))
    """
    test_is_not_valid_pin method

    Checks that the pin does not matche the account and returns False.
    """
    def test_is_not_valid_pin(self):
        #Check for an invalid PIN
        self.assertFalse(self.account.is_valid_pin("5678"))
"""
TestBank class

Stores setup and testing methods for addAccountToBank, removeAccountFromBank, findAccount, and addMonthlyInterest.
"""
class TestBank(unittest.TestCase):
    """
    setUp method

    creates bank and three account objects for the other methods to test against.
    """
    def setUp(self):
        self.bank = Bank()
        self.account1 = Account("Ryan", "Richardson", "123456789", "1234")
        self.account2 = Account("Mike", "Smith", "987654321", "4321")
        self.account3 = Account("Joe", "Johnson", "111111111", "1111")
    """
    test_addAccountToBank method

    Attempts to add one of the account to the bank and see if it is true.
    """
    def test_addAccountToBank(self):
        # Tests that an account can be added to an empty bank
        self.assertTrue(self.bank.addAccountToBank(self.account1))
    """
    test_addAccountToBank_more_than_100 method

    Creates a bank that is full and tries to add another account which will not be allowed.
    """
    def test_addAccountToBank_more_than_100(self):
        # Tests that adding more than 100 accounts fails
        for i in range(Bank.max_accounts):
            new_account = Account("Jacob", "Parker", "000000000", "0000")
            self.bank.addAccountToBank(new_account)
        self.assertFalse(self.bank.addAccountToBank(self.account2))
    """
    test_removeAccountFromBank method

    Checks if an account is removed after it is added.
    """
    def test_removeAccountFromBank(self):
        # Tests removing an account that is in the bank
        self.bank.addAccountToBank(self.account1)
        self.assertTrue(self.bank.removeAccountFromBank(self.account1))
    """
    test_removeAccountNotInBank method

    Tries to remove an account that is not in the bank which will not be allowed.
    """
    def test_removeAccountNotInBank(self):
        # Tests removing an account that is not in the bank
        self.assertFalse(self.bank.removeAccountFromBank(self.account2))
    """
    test_findAccount method

    Adds an account to the bank then tries to find it.
    """
    def test_findAccount(self):
        # Tests finding an account that is in the bank
        self.bank.addAccountToBank(self.account1)
        self.assertEqual(self.bank.findAccount(self.account1.get_account_number()), self.account1)
    """
    test_findAccountNotInBank method

    Tries to find an account that is not in the bank and returns None.
    """   
    def test_findAccountNotInBank(self):
        # Tests finding an account that is not in the bank
        self.assertIsNone(self.bank.findAccount(self.account2.get_account_number()))
    """
    test_addMonthlyInterest method

    Adds monthly interest to two accounts at a 2% rate.
    """   
    def test_addMonthlyInterest(self):
        # Test adding interest to two accounts
        self.bank.addAccountToBank(self.account1)
        self.bank.addAccountToBank(self.account2)
        self.account1.set_balance(1000)
        self.account2.set_balance(2000)
        self.bank.addMonthlyInterest(2)
        self.assertAlmostEqual(self.account1.get_balance(), 1166.67, 2)
        self.assertAlmostEqual(self.account2.get_balance(), 2333.33, 2)
"""
TestBankUtility class

Stores  methods for isNumeric, convertFromDollarsToCents, and generateRandomInteger.
"""
class TestBankUtility(unittest.TestCase):
    """
    test_isNumeric_valid method

    Tests if the input is numeric.
    """  
    def test_isNumeric_valid(self):
        # tests for isNumeric valid input
        self.assertTrue(BankUtility.isNumeric('12345'))
    """
    test_isNumeric_invalid method

    Tests if the input is not numeric.
    """  
    def test_isNumeric_invalid(self):
        # tests for isNumeric invalid input
        self.assertFalse(BankUtility.isNumeric('abc123'))
    """
    test_convertFromDollarsToCents_positive method

    Tests input or user balance is positive and diplays the correct answer.
    """  
    def test_convertFromDollarsToCents_positive(self):
        # tests a positive balance conversion
        self.assertEqual(BankUtility.convertFromDollarsToCents(10.50), 1050)
    """
    test_convertFromDollarsToCents_negative method

    Tests input or user balance is negative and diplays an error.
    """  
    def test_convertFromDollarsToCents_negative(self):
        # tests a negative balance conversion
        self.assertIsNone(BankUtility.convertFromDollarsToCents(-10.50))
    """
    test_generateRandomInteger_min method

    Tests that the minimum that can be generated is 1.
    """  
    def test_generateRandomInteger_min(self):
        # tests a minimum value from the range
        self.assertGreaterEqual(BankUtility.generateRandomInteger(1, 10), 1)
    """
    test_generateRandomInteger_max method

    Tests that the maximum that can be generated is 10.
    """  
    def test_generateRandomInteger_max(self):
        # tests a maximum value from the range
        self.assertLessEqual(BankUtility.generateRandomInteger(1, 10), 10)

if __name__ == '__main__':
    unittest.main()
"""
CoinCollector class

Creates a dictionary of coins with correlated values and stores a method that parses them.
"""
class CoinCollector:
    """
    parseChange method

    Iterates through the coins that will be inputted. Assigns their value and returns the sum of them all.
    """
    def parseChange(self, coins):
        # Dictionary set to the variable coin_values.
        coin_values = {
            'P': 0.01,
            'N': 0.05,
            'D': 0.10,
            'Q': 0.25,
            'H': 0.50,
            'W': 1.00
        }
        # Starts at 0 cents then iterates through to assign values to each letter and adds that on.
        total_cents = 0
        for coin in coins:
            if coin in coin_values:
                total_cents += coin_values[coin]
            else:
                # Raises error if the key is not in the dictionary.
                raise ValueError
            print("Invalid Coin")
        return total_cents

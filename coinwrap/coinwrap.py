#Coin Estimator By Weight

#Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
#Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all of their money.
# Subgoals:
# Round all numbers printed out to the nearest whole number.
# Allow the user to select whether they want to submit the weight in either grams or pounds.

# Using Euro measures - https://en.wikipedia.org/wiki/Coin_wrapper#Eurozone, limiting to 20c upward

#Color	Denomination	Count	Total Value	Weight (g)

#Orange	20c	40	€8.00	233.2
#Green	50c	40	€20.00	313.2
#Yellow	€1	25	€25.00	189.3
#Purple	€2	25	€50.00	207.5

import time

EURO_VALUES = { ".20":{"value": 0.20, "coin_weight": 5.83, "wrap_count": 40, "wrap_col": "Orange", "wrapper_total": 8},
                ".50":{"value": 0.50,"coin_weight": 7.85, "wrap_count": 40, "wrap_col": "Green", "wrapper_total": 20},
                "1":{"value": 1.00,"coin_weight": 7.572, "wrap_count": 25, "wrap_col": "Yellow", "wrapper_total": 25},
                "2":{"value": 2.00,"coin_weight": 8.292, "wrap_count": 25, "wrap_col": "Purple", "wrapper_total": 50},
                }

def counter(user_coins):
    result = {}
    for x in user_coins:
        user_results = {"coin_num": 0, "coin_val": 0.00, "wrap_num": 0, "wrap_col": "", "leftover": 0}
        coins = int((user_coins[x] / EURO_VALUES[x]["coin_weight"]))
        user_results["coin_num"] = coins
        user_results["coin_val"] = eur((coins * EURO_VALUES[x]["value"]))
        wrappers_needed = int((coins / EURO_VALUES[x]["wrap_count"]))
        user_results["wrap_num"] = wrappers_needed
        user_results["wrap_col"] = EURO_VALUES[x]["wrap_col"]
        user_results["leftover"] = (coins - (wrappers_needed * EURO_VALUES[x]["wrap_count"]))
        result[x] = user_results
    return result


def eur(value):
    """Format value as EUR."""
    float(value)
    return f"€{value:,.2f}"

def main():
    print("\nWelcome to the coin counter.\n")
    #time.sleep(2)
    print("""Please enter the weight of coins in grams you have for each of the following values: 20c, 50c, €1, €2.\n
    If you have none of that type of coin, enter 0 in that postition.\n""")
    #time.sleep (3)
    twenty_coins = input("What is the weight of 20c coins you have? ")
    fifty_coins = input("What is the weight of 50c coins you have? ")
    one_coins = input("What is the weight of €1 coins you have? ")
    two_coins = input("What is the weight of €2 coins you have? ")
    user_weights = {".20": float(twenty_coins), ".50": float(fifty_coins), "1": float(one_coins), "2": float(two_coins)}
    results = counter(user_weights)
    print("\nResults: \n")
    file = open("receipt.txt","w")
    file.write("Results:\n\n")
    for y in results:
        one_result = results[y]
        one_result.update({"type" : eur(float(y))})
        message= (
                f"You have {one_result['coin_num']} of {one_result['type']} coins worth {one_result['coin_val']}. "
                f"You will need {one_result['wrap_num']} {one_result['wrap_col']} wrappers. "
                f"You will have {one_result['leftover']} leftover coins."
                )
        print(message)
        file.write(message + "\n")
    file.close()

if __name__ == "__main__":
    main()
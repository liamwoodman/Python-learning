"""
Menu Calculator
Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. S
ince your restaurant only sells 9 different items, you assign each one to a number, as shown below.

Chicken Strips - $3.50
French Fries - $2.50
Hamburger - $4.00
Hotdog - $3.50
Large Drink - $1.75
Medium Drink - $1.50
Milk Shake - $2.25
Salad - $3.75
Small Drink - $1.25
To quickly take orders, your program should allow the user to type in a string of numbers
and then it should calculate the cost of the order. For example, if one large drink, two small drinks,
two hamburgers, one hotdog, and a salad are ordered, the user should type in 5993348,
and the program should say that it costs $19.50.
Also, make sure that the program loops so the user can take multiple orders without having to restart the program each time.

Subgoals:
If you decide to, print out the items and prices every time before the user types in an order.
Once the user has entered an order, print out how many of each item have been ordered, as well as the total price.
If an item was not ordered at all, then it should not show up.

NOTES:
Need to add a 'try/except' logic to this in order to reject any orders of 0 or 9 (as list is only 1-8).
Atm will give a key error.

"""
from collections import Counter

MENU_ITEMS = {
        "1": {"name": "Chicken Strips", "price": 3.50},
        "2": {"name": "French Fries", "price": 2.50},
        "3": {"name": "Hamburger", "price": 4.00},
        "4": {"name": "Salad", "price": 3.75},
        "5": {"name": "Large Drink", "price": 1.75},
        "6": {"name": "Medium Drink", "price": 1.50},
        "7": {"name": "Small Drink", "price": 1.25},
        "8": {"name": "Milk Shake", "price": 2.25}
    }

def take_order():
    bad_input = True
    #bad_item = False
    #order_list = []

    while bad_input:
        order = input("What is the order? Type menu if you would like to see the menu. Order: ")

        """
        Attempt to pull out of key values but still getting through somehow!

        for item in order:
            if int(item) > 0 or int(item) < 9:
                print(item, bad_item)
                bad_item = True

            order_list.append(item)
        """

        if order.lower() == "menu":
            print("\nHere's the Menu:\n")
            for item_id, item_info in MENU_ITEMS.items():
                print(item_id + ": " + str(item_info["name"]) + ", " + str(eur(item_info["price"])))
            print("\n")
        elif not order.isnumeric():
            print("\nBad entry detected. Please enter your order again.\n")
        #elif bad_item == True:
            #print("\nMenu item not detected. Please enter your order again.\n")

        else:
            bad_input = False
        return order

def create_order(order):
    order_list = []
    for y in order:
        order_list.append(y)
    counted_list = Counter(order_list).most_common()

    total = 0.00
    user_order = []
    for item, count in counted_list:
        print(item, count)
        items_amount = (MENU_ITEMS[item]["price"] * count)
        items_ordered = MENU_ITEMS[item]["name"], count, items_amount
        user_order.append(items_ordered)
        total += items_amount
    return user_order, total


def again():
    check = input("Would you like to take another order? Y/N: ")
    if check.lower() == "y":
        pass
    elif check.lower() == "n":
        exit()
    else:
        print("Please press either Y or N")
        again()


def eur(value):
    """Format value as EUR."""
    float(value)
    return f"€{value:,.2f}"

def main():
    print("\nWelcome to the menu calculator.\n")
    while True:
        order = take_order()
        formatted_order, total = create_order(order)
        print("The order is: \n")
        for counter, item in enumerate(formatted_order):
            print("Item " + str(counter + 1) + ": " + str(item[1]) + "x " + str(item[0]) + " - " + str(eur(item[2])))
        print("\nThe total is " + str(eur(total)) + "\n")
        again()


if __name__ == "__main__":
    main()
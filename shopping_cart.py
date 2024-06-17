# create a shopping cart application that adds items to a shopping cart (a dictionary)
# the key will be the item, the value will be the price

shopping_cart = {}

def add_item(cart):
    # store the item as a key
    item = input("What would you like to add to your cart?")
    # taking quantity and price so we can see how much that number of items costs
    quantity = int(input(f"How many of {item} would you like? "))
    price = float(input(f"How much does {item} cost? "))
    # total price as a value
    total_item_price = quantity * price

    # gives our dictionary a key of the item and a value of the price * quantity
    cart[item] = total_item_price

def remove_item(cart):
    item = input("What would you like to remove from your cart? ")
    # checking if our item is not in the cart
    if item not in cart:
        # if its not telling the user the item doesnt exist
        print("You dont have that item in your cart")
    else:
        # otherwise, it does exist and we can delete it
        del cart[item]

def view_cart(cart):
    # looping through the key, value pairs in our dictionary
    for item, price in cart.items():
        # printing out each item with its price set in the add_item function
        print(f"{item}: ${price}")
        # call the calculate_total function to add all the values (prices) in our dictionary
    total = calculate_total(cart)
    print(f"Your current cart total: ${total}")
    

def calculate_total(cart):
    prices = cart.values()
    total = sum(prices)
    return total



def main(cart):
    while True:
        response = input("What would you like to do? 1. add 2. remove 3. view 4. quit and view total? ")

        if response == "1":
            add_item(cart)
        elif response == "2":
            remove_item(cart)
        elif response == "3":
            view_cart(cart)
        elif response == "4":
            print("Here is your total: ")
            print(f" - ${calculate_total(cart)}")
        else:
            print("Please enter a valid response!")
# main(shopping_cart)

# Create an empty dictionary representing a garage
# key - item, value - location
# write functions to add, remove, and view your items in the garage
# create driver code to ask the user what they would like to do within the garage
# BONUS POINTS for updating item locations in the garge]


greeting = "hello"

another = "hello there"

if greeting in another:
    print("yes")
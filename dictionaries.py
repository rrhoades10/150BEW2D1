# a dictionary is an ordered collection of key value pairs


# declaring an empty dictionary - {}
kitchen = {}

print(kitchen)
print(type(kitchen))

# storing key value pairs in dictionaries
kitchen = {
    # key   :   value
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"
}
print(kitchen)

# Keys in a dictionary should be unique
kitchen = {
    # key   :   value
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf",
    "Spoons": "Bottom Drawer"
}
print(kitchen)

# what can we use as keys in a dictionary?
#immutables types
int_dict = {
    1: "first key",
    2: "second key",
    3: "third key",
    3.4: "3.4th key"
}
print(int_dict)

# Accessing values in a dictionary
# dictionary_name[key]
kitchen = {
    # key   :   value
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"
}
#                  dict_name[key]
spoon_location = kitchen["Spoons"] #this gives us the value of Top Drawer
print(spoon_location)
print(kitchen["Plates"])

# be careful with using integers as keys becasue it makes it difficult
# to distinguish between dictionaries and lists
integers = {
    1: "first key",
    2: "second key",
    3: "third key",
    3.4: "3.4th key"
}
print(integers[1])

# using number strings as keys 
integers = {
    "1": "first key",
    "2": "second key",
    "3": "third key",
    "3.4": "3.4th key"
}
print(integers["2"])

# KeyError - happens when a key doesnt exist in a dictionary
kitchen = {
    # key   :   value
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"
}
# print(kitchen["bowls"]) bowls is not a key in our dictionary - KeyError

# dict.get() <- return a value from a ky in our dictionary
# with no second argument, .get() will return none if the key isn't found
potential_item = kitchen.get("Blender")
print(potential_item)
# returnign the value of a found key
print(kitchen.get("Cups", "you dont have that item")) # Top Shelf
# ^^ only returns the second argument, if the key is not found ^^
# .get() with a second argument
print(kitchen.get("Toast", "You don't have that item in your kitchen"))

# Adding and Updating our dictionary
community_center = {
    "Smash Tournament": "7 pm",
    "Yoga": "5 am"
}
print(community_center)

# Adding to a dictionary
# dict[key to be added] = value to add at that key
# adding knitting to the dictionary
community_center["Knitting"] = "9 am"
print(community_center)
community_center["Zumba Session"] = "8 am"
print(community_center)
community_center["Art Gallery"] = "8 pm"
print(community_center)

# what if they key already exists?
# it updates the key to the new value
# updating a key, value pair
community_center["Yoga"] = ["6 am", "9 pm"]
# if they key already exits in the dictionary, it will set the key to the new value
print(community_center)

# creating a counter dictionary
counter_dict = {}
pokemon_cards = ["Charmander", "Blissey", "Jynx", "Jynx", "Jynx", "Milotic", "Milotic", "Blissey", "Charmander", "Jynx"]
for card in pokemon_cards:
    # if the card is in the dictionary already
    # then we've added it and need to increment the number of occurrences by 1
    if card in counter_dict:
        # counter_dict[cartd] = counter_dict[card] + 1
        counter_dict[card] += 1
    # first occurence of the card we set the calue to one
    else:
        counter_dict[card] = 1
print(counter_dict)

# removing things from a dictionary
# dict.pop(thing_to_be_removed, value_if_not_found)
inventory = {"Apples": 30, "Oranges": 20, "Bananas": 15}
removed_item = inventory.pop("Apples") # return the value of the popped key
print(removed_item) # 30
print(inventory)
# popping a key that doesn't exist
# attempted_removal = inventory.pop("Canteloupe") # KeyError becuase Canteloupe is not in the dictionary
# popping a key that doesn't exist BUT giving pop a second argument
removed_value = inventory.pop("Canteloupe", "That doesn't exist to be removed")
print(removed_value)

# dict.popitem() -> remove and returns the last key, value pair added to the dictionary
inventory = {"Apples": 30, "Oranges": 20, "Bananas": 15}
inventory["Canteloupe"] = 25
print(inventory)
last_item_removed = inventory.popitem()
print(last_item_removed)
print(inventory)
# as of python 3.7 - dictionaries are ordered
# before dictionaries were orderd popitem() would pop a random item from the list
last_item_removed = inventory.popitem()
print(last_item_removed)
print(inventory)

# del dict["key"] - deletes entire key, value pair
inventory = {"Apples": 30, "Oranges": 20, "Bananas": 15}
del inventory["Oranges"]
print(inventory)

# dict_.clear() -> clears all items in a dictionary
inventory = {"Apples": 30, "Oranges": 20, "Bananas": 15}
inventory.clear()
print(inventory)

# dict.keys() -> list of all the keys in a dictionary
contact = {
    "name": "Alice", "age": 30, "email": "alice@gmail.com"
}
print(contact.keys())
for key in contact.keys():
    print(key)

# looping through keys and using them to acces the value's
print("Here is your contact info")
for key in contact.keys():
    #     each key,   accessing the value for each key
    print(f"{key}: {contact[key]}")

# by default looping through a dictionary accesses its keys
for info in contact:
    print(f"{info}: {contact[info]}")

# dict.values() -> list all of the values in a dictionary
temps = {"Monday": 97, "Tuesday": 92, "Wednesday": 94}
print(temps.values())
print("Here is the forecast for the next 3 days")
for temp in temps.values():
    print(temp)

#dict.items() -> return a list of tuples with the key in the first position and the value in the second position
book_ratings = {"1984": 4.5, "LOTR: Return of the King": 5, "Brave New World": 4.3}
print(book_ratings.items())
for item in book_ratings.items():
    print(item) #prints each tuple out from the list of items

for book, rating in book_ratings.items():
    print(f"{book} has a rating of {rating}.")

# using sorted on a dictionaries keys or values
colors = {"red": 2, "blue": 5, "green": 1}
print(sorted(colors)) # sorts just the keys
print(sorted(colors.keys()))
# sorting the values
print(sorted(colors.values()))
# sorting items
print(sorted(colors.items()))

# dict.updated({"key": "value"})
kitchen = {
    # key   :   value
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"
}
# updating a current key - if the key already exists, we update it
kitchen.update({"Cups": "Middle Shelf"})
print(kitchen)
# if the key doesn't exist, we can add it
kitchen.update({"Air Fryer": "Counter Top"})
print(kitchen)
# updating a dictionary with more than one key value <- sets apart from the regular assignment
counter_top_stuff = {
    "Toaster": "Counter Top",
    "Cutting Board": "Counter Top",
    "Rice Cooker": "Counter Top",
    "Flowers": "Counter Top"                      
}
kitchen.update(counter_top_stuff)
print(kitchen)

# dict.setdefault()
inventory = {"apples": 30, "oranges": 40}
bananas = inventory.setdefault("bananas", 0)
print(bananas)
print(inventory)
apples = inventory.setdefault("apples")
print(apples)
print(inventory)
# with no second argument - add the key to the dictionary with a value of None
inventory.setdefault("canteloupe")
print(inventory)
# print(inventory[1:2]) TypeError cant slice a dictionary


# Create a dictionary with at least 2 key value pairs in it to start
# elaborate on the kitchen example or create your own collection
# add two new items with assignment dict[key] = value
# use .update to add at least 3 new items to your dictionary
# delete as many items as youd like using either pop or del

library = {"Harry potter":"JK Rollen",
           "Twilight":"Stephany Meyer",
           "Green eggs and ham":"Dr sues"
}

new_stuff = {
    "Chronicles of Narnia": "CS Lewis",
    "Spiderman": "Stan Lee",
    "Ironman": "Stan Lee"
}
print(library)
library.update(new_stuff)
print(library)
library.update({"Green eggs and ham": "Dr. Seuss"})
print(library)
# library.update({"Chronicles of Narnia": "CS Lewis"})
# print(library)
# library.update({"Spider"},{"Stan Lee"})
# print(library)
# library.update({"Ironman"},{"Stan Lee"})
# print(library)

blakes_dict = {
    'name': 'Blake',
    'age': 19
}
blakes_dict['height'] = '6ft'   
blakes_dict['weight'] = '178lbs'
blakes_dict.update({'hair': 'brown', 'eyes': 'blue', 'knuckles': 'unpopped'})
blakes_dict.pop('knuckles')
print(blakes_dict)
# response = input("What information would you like to see about Blake? ")
# print(blakes_dict["Height"]) <- KeyError because of case sensitivity 
# blakes_dict["Height"] = "6ft 1" this adds a whole new item to the dictionary
# print(blakes_dict)


# NESTING COLLECTIONS IN DICTIONARIES
library = {
    "Fantasy": ["Harry Potter", "The Hobbit", "LOTR"],
    "Science Fiction": ["Dune", "Star Wars: Annihilation"],
    "Mystery": ["Sherlock Holmes", "And Then There Were None"]
}

# accessing a list that is as value in a dictionary
fantasy_books = library["Fantasy"]
print(fantasy_books)
for book in fantasy_books:
    print(book)

for book in library["Science Fiction"]:
    print(book)

# indexing into a list in a dictionary
print(library["Mystery"][1])
# ^ indexing into a list that is a value, using the key to get to the value
print(library["Fantasy"][2])

# adding an item to a list in a dictionary
library["Science Fiction"].append("The Martian")
print(library)

# looping through a dictionaries items and then the contents of its values - if they're lists

for genre, books in library.items():
    print(f"Here are the books for the {genre} genre: ")
    for book in books:
        print(f" - {book}")

# for item in library.items():
#     print(item)


# Dictionaries in lists
art_gallery = [
    {"Title": "Starry Night", "Artist": "Van Gogh", "Year": 1889},
    {"Title": "The Scream", "Artist": "Munch", "Year": 1893},
    {"Title": "Guernica", "Artist":"Picasso", "Year": 1937}
]
print(art_gallery)
# appending another dictionary to the list
art_gallery.append({"Title": "The Persistence of Memory", "Artist": "Dali", "Year": 1931})

print(art_gallery)

# looping through a list of dictionaries
for artwork in art_gallery:
    print(artwork["Title"], artwork["Artist"], artwork["Year"])

# looping through the list with dict.items()
for artwork in art_gallery:
    for info, value in artwork.items():
        print(f"{info}: {value}")


# Dictionaries in Dictionaries
museum_exhibits = {
    # each key represent a museum exhibit
    "Ancient Egypt":{
        "Artifacts": ["Sphinx", "Pyramids"],
        "Famous Pharoahs": ["Tutankhamun", "Cleopatra"]
    },
    "Renaissance Art": {
        "Notable Artists": ["Leonardo", "Michelangelo", "Rafael", "Donatello"],
        "Key Works": ["Mona Lisa", "The Last Supper"]
    }
}

print(museum_exhibits)
# adding a new key, value pair to a nested dictionary
museum_exhibits["Ancient Egypt"]["Recent Discoveries"] = ["New Tomb", "Ancient Slabs"]
print()
print(museum_exhibits)
museum_exhibits["Ancient Egypt"]["Famous Pharoahs"].append("Atem")
print(museum_exhibits)

# looping through ALL the items
for exhibit, details in museum_exhibits.items():
    print(f"Exhibit: {exhibit}")
    for section, items in details.items():
        print(f" - section {section}")
        for artifact in items:
            print(f"    -   {artifact}")

# setting "checkpoints" within nested dictionaries

ancient_egypt = museum_exhibits["Ancient Egypt"]
print(ancient_egypt)
for section , items in ancient_egypt.items():
    print(section, items)



# NOTE: These are notes on how to remove items from a dictionary.
# NOTE: methods bank: pop(); popitem(); clear(); 'del' keyword; 


# NOTE: pop() - removes  item w/specified key name:
fruits = {
    "color": "yellow-orange",
    "shape": "round",
    "type": "tangerine",
    "taste": "sweet",
    "location": "Florida",
    "season": "summer"
}
fruits.pop("location")     # removes {"location": "Florida"}
print(fruits)       



# NOTE: popitem() - removes last inserted item:
fruits.popitem()        # should remove {"season": "summer"}
print(fruits)



# NOTE: 'del' keyword - removes item with specified key name: 
del fruits["taste"]
print(fruits)

# 'del' keyword can also delete the dictionary entirely: 
# del fruits
# print(fruits)       # will cause an error


# NOTE: clear() - empties the dictionary:
fruits.clear()
print(fruits)


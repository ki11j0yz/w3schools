# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered, unchangeable and allows duplicates
 

# Tuples are written with round brackets
tuple1 = ("apple", "banana", "cherry")
print(tuple1)

# Tuple items are indexed, the first item has index [0], second item has index [1], etc.
print(tuple1[2])


# Tuples are unchangeable, meaning we cannot change, add or remove items after the tuple has been created.
# For example: 

# tuple1 = ("gang", 34, "potato")
# tuple1[0] = "charity"
# #print(tuple1)
# these lines of code will bear a "type error"

# In a list:
list1 = ["apple", "cherry", "mango"]
print(list1)
list1[0] = "banana"
print(list1)



# NOTE: methods: index(), count(), add(), update(), remove(), delete(), discard(), get()
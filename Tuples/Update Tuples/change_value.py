# NOTE: Tuples are unchangeable, or 'immutable' but there is a workaround by changing the tuple to a list, changing the list, and then converting the list back to a tuple. 

tuple1 = ("math", "geography", "science", "history", "english", "sociology")
print(tuple1)
tuple_to_list = list(tuple1)    # NOTE: changing the tuple to a list format
tuple_to_list[3] = "gym"
list_to_tuple = tuple(tuple_to_list)    # NOTE: changing list back to a tuple
print(list_to_tuple)

# NOTE: While this method is only changing a single index, you can add tuples to tuples, so if you wanted to add an item, just create a new tuple
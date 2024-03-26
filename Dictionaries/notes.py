# NOTE: Dictionaries are used to store data values in key:value pairs using curly brackets {}
# NOTE: Dictionaries are ordered, changeable and exclude duplicates.
# NOTE: Python 3.7 and up are ordered, Python 3.6 and earlier are unordered.
# NOTE: Dictionaries are of data type(dict)

this_dict = {
    "Age": "35", 
    "Sex": "Male", 
    "Location": "USA"
}
print(this_dict)


# NOTE: Dict itmes - presented in key:value pairs and can be referred to by using 'key' name: 
print(this_dict["Age"])


# NOTE: Duplicates - they are excluded:
new_dict = {
    "Age": "35",
    "Sex": "Male",
    "Location": "USA",
    "Location": "California"
} 
print(new_dict)


# NOTE: Dict length with len():
print(len(new_dict))            # notice the duplicate is excluded


# NOTE: Dict data types:
that_dict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colores": ["red", "white", "blue"]
}
print(that_dict)


# NOTE: dict() constructor - you can construct a dictionary by defining it's type with 'dict'
the_dict = dict(name = "john", age = 36, country = "Norway")
print(the_dict)



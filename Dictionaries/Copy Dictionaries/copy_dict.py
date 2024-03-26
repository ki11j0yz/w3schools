# NOTE: How to copy a Python dictionary.
# NOTE: you can not copy a dictionary by setting obj_dict1 = obj_dict2, because obj_dict2 will only be a reference to obj_dict1, and changes made to obj_dict1 will automatically update in obj_dict2...
# NOTE: methods band: copy(); dict(); 

obj_dict1 = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Cahrlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel"
}

obj_dict2 = {
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November", 
    "O": "Oscar",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}


# NOTE: copy() - make a copy of a dictionary:
obj_copy = obj_dict1.copy()
print(obj_copy)


# NOTE: dict() - built in function, makes a copy:
obj_dict = dict(obj_dict2)
print(obj_dict)



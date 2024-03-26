# NOTE: these notes will describe, in detail, different ways for looping through dictionaries.
# NOTE: return values are the 'keys' of the dictionary, but there are methods to return the 'values' as well. 
# NOTE: methods bank: values();


obj1 = {
    "A": "Aardvark",
    "B": "Banana",
    "C": "Canary",
    "D": "Dog",
    "E": "Elephant",
    "F": "Fox",
    "G": "Gravy",
    "H": "Helicopter"
}


# NOTE: 'for' loop - print all 'key' names:
for x in obj1:
    print(x)


# NOTE: 'for' loop - print all 'value' names:
for x in obj1:
    print(obj1[x])
    
    
# NOTE: values() - returns values:
for i in obj1.values():
    print(i)


# NOTE: keys() - returns the fucking keys:
for i in obj1.keys():
    print(i)     


# NOTE: items() - loops throgh both keys and values:
for a, b in obj1.items():
    print(a, b)

    
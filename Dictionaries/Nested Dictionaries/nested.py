# NOTE: Understanding how nested dictionaries work.
# NOTE: A nested dictionary is a dictionary within a dictionary. Dictionaryception.

# NOTE: Create a dictionary that contains three other dictionaries: 
big3 = {
    "Tech Giant #1": {
        "Name": "Google",
        "Founded": 1998
    },
    
    "Tech Giant #2": {
        "Name": "Microsoft",
        "Founded": 1975
    },
    
    "Tech Giant #3": {
        "Name": "Apple",
        "Founded": "1976"
    }
}


# NOTE: create 3 dictionaries, then create one dictionary that will contain the other 3:
google = {
    "Name": "Google",
    "Type": "Search Engine",
    "Founded": 1998
}

microsoft = {
    "Name": "Microsoft",
    "Type": "Micro-computers",
    "Founded": 1975
}
 
apple = {
    "Name": "Apple",
    "Type": "Micro-computers",
    "Founed": 1976
}


tech_giants = {
    "Tech Giant #1": google,
    "Tech Giant #2": microsoft,
    "Tech Giant #3": apple
}

print(tech_giants)


# NOTE: Accessing items from a nested dictionary - use the name of the dicionaries, starting with the outer one first:
print(tech_giants["Tech Giant #1"]["Founded"])

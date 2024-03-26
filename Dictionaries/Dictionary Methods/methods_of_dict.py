# NOTE: I will try to figure out these Python Dictionary methods, as always, here's a reference bank:

# NOTE: methods bank: clear(); copy(); fromkeys(); get(); items(); keys(); pop(); popitem(); setdefautlt(); update(); values();

# practice dictionary: 
python = {
    "Name": "Python",
    "Founded by": "Guido Van Rossum",
    "Founded in": 1989
}

golang = {
    "Name": "GoLang",
    "Founded by": "Google",
    "Founded in": 2009
}

perl = {
    "Name": "Perl",
    "Founded by": "Larry Wall",
    "Founded in": 1987
}

developers = {
    "Language #1": python,
    "Language #2": golang,
    "Language #3": perl
}

# NOTE: clear() - removes all elements from the dictionary:

# developers.clear()
# print(developers)         # output = {}


# NOTE: copy() - returns a copy of the specified dictionary:

# x = developers.copy()
# print(x)


# NOTE: fromkeys(); syntax: dict.fromkeys(keys, value) - returns a dictionary with the specified keys:value
coordinates = ('x', 'y', 'z')
x = 0
coord_dict = dict.fromkeys(coordinates, x)
print(coord_dict)


# NOTE: get(); syntax: dictionary.get(keyname, value) - returns value of item w/specified key:
a = golang.get("Founded in")
print(a)

b = golang.get("", 2009)
print(b)



# NOTE: items(); syntax: dictionary.items() - returns a view object which contains key:value pairs of the dictionary, as tuples in a list - the view object will reflect any changes done to the dictionary:

c = perl.items()
print(c)        # dict_items([('Name', 'Perl'), ('Founded by', 'Larry Wall'), ('Founded in', 1987)])


# NOTE: keys(); syntax: dictionary.keys() - returns a view object which contains the keys fo the dict, as a list: 
d = python.keys()
print(d)        # dict_keys(['Name', 'Founded by', 'Founded in'])


# NOTE: pop(); syntax: dicitionary.pop(keyname, defaultvalue) = removes specified item from dictionary:
perl.pop("Name")
print(perl)


# NOTE: popitem(); syntax: dictionary.popitem() - removes last inserted item of dictionary, returns as tuple:
perl.popitem()
print(perl)


# NOTE: setdefault(): returns value of specified item with specified key - if key does not exist, insert the key with specified value: syntax: dicitionary.setdefault(keyname, value):
e = perl.setdefault("Founded in", 1987)
print(e)
print(perl)         # prints updated perl dictionary


# NOTE: update(): inserts specified items to the dictionary - specified items can be a dictionary themselves, or an iterable object with key:value pairs: syntax: dictionary.update(iterable):
perl.update({"Name:": "Perl"})
perl.update([("Key", "Value"), ("Keys", "Values")])
print(perl)


# NOTE: values(): returns a list of all the values in the dictionary: syntax: dictionary.values():
all_values = developers.values()
for i in all_values:
    print(i)
    
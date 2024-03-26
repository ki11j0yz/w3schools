# NOTE: Bank of methods: get(); keys(); values(); items(); 

# NOTE: access items by referring to key name inside square brackets:
first_dict = {
    "type": "sweatshirt",
    "brand": "Addidas",
    "material": "fleece",
}
x = first_dict["brand"]
print(x)



# NOTE: get() method - it gets shit
a = first_dict.get("brand")
print(a)



# NOTE: Get Keys - keys() method will return list of all keys in dict:
b = first_dict.keys()
print(b)


# NOTE: list of keys is a view of dict, means any changes done to dict will be reflected in keys list:
c = first_dict.keys()
print(c)                                        # before change
first_dict["material"] = "flannel"
print(first_dict)                               # after change



# NOTE: Get Values - values() method will return list of all values in dict:
d = first_dict.values()
print(d)

# making a change by adding key:value pair to first_dict: 
first_dict["color"] = "red"
print(first_dict.values())



# NOTE: Get Items - items() method will return each item in a dict, as tuples in a list: 
e = first_dict.items()
print(e)

# making a change by adding key:value pair: 
f = first_dict.items()
print(f)
first_dict["type"] = "jacket"
print(first_dict.items())


# NOTE: Check if Key exists using 'in' keyword: 
if "jeans" in first_dict:
    print("Yes")
else:
    print("No")
    



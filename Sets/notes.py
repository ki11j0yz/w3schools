# NOTE: written with curly brackets {}, they are unordered, unchangeable*, *unindexed, no duplicates
# NOTE: UNCHANGEABLE *set ITEMS are unchangeable, however you can add and remove items
# NOTE: UNINDEXED *set items cannot be referred to by index or key


### UNINDEXED
myset = {"Pink", "BeYonce", "Ke$ha"}
#print(myset[2])             # NOTE: UNINDEXED: will output ERROR




### UNORDERED
set1 = {"List", "Dictionary", "Tuple"}
#print(set1)                 # NOTE UNORDERED: output order may vary



### UNCHANGEABLE    
set2 = {"horse", "pig", "goat"}
#set2.insert(1, "cow")       # NOTE: this does not work with sets, or tuples for that matter. 
#print(set2)


### Add/Remove
dogs = {"labrador", "husky", "beagle"}
dogs.add("doberman")        # NOTE: you can add() items
dogs.remove("beagle")       # NOTE: you can remove() items
print(dogs)



### DUPLICATES
dupl = {"comma", "apostrophe", "colon", "comma"}
print(dupl)                 # NOTE: duplicate is ignored at output
boolean = {1, True}         # NOTE: the values 'True' and '1' are considered duplicates in sets
boolean2 = {False, 0}       # NOTE: vice versa with 'False' and '0' - considered duplicates
print(boolean)         

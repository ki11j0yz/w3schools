# NOTE: you can not access items in a set by referring to index or key
# NOTE: however you can loop through a set with a 'for' loop, or ask if a specified value is present by using the 'in' keyword: 

### Access by 'for' loop:
alcohol = {"whiskey", "beer", "vodka"}
for i in alcohol:
    print(i)
    
    

### Access by 'in' keyword:
set1 = {"set{}", "tuple()", "dictionary{}", "list[]"}
print("tuple()" in set1)

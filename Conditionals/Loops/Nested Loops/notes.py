# NOTE: nested loops are loops inside of loops. The inner loop is executed once for each iteration of the outer loop.

# print each adjective for every language:
adj = ("complex", "effective", "efficient")
fruits = ("Ruby", "GoLang", "Perl")

for x in adj:
    for y in fruits:
        print(x, y)



# iterating over multidimensional data structures:
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for x in list_of_lists:
    for y in x:
        print(y)
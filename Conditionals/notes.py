# NOTE: Conditionals, Loops & Iterators, Polymorphism
# NOTE: Python If...Else statement - used to execute both the True and False parts of a given condition.
# NOTE: Python supports the usual logical conditions from mathematics: 

# logical_conditions = {
#     "Equals": "a == b",
#     "Not Equals": "a != b ",
#     "Less than": "a < b",
#     "Greater than": "a > b",
#     "Greater than/Equal to": "a >= b"
# }

# NOTE: these conditions can be used in many different ways, most commonly in 'if-statements' and loops:

x = 1000
y = 500
if x > y:
    print("x is bigger than y")

# NOTE: notes about how I constructed the above if statement, and also notes about proper indentation (especially during an if-statement)



# NOTE: Shorthand 'if': if you only have 1 statement to execute, you can put it on the same line as the 'if' statement: 
if x > y: print("x is greater than y gotdammit")


# NOTE: Shorthand 'if-else': "same as above":
print("x") if x > y else print("y")         # should print 'X'


# NOTE: Ternary Operators a.k.a. Conditional Expressions: 
# NOTE: you can also have mult. else statements on the same line: 
print("x") if x > y else print("=") if x == y else print("y")



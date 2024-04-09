# NOTE: Arbitrary Arguments, *args:
# if an unknown amount of args is passed into your fn, add '*' before the parameter name in the fn definition:

def my_function(*cars):
    print("The fastest car is " + cars[2])
    
my_function("Mustang", "Chevelle", "Corvette")
print("\n")

# notice how args are basically in a list, and print statement in fn uses indexing to pick from args "kids[2]"

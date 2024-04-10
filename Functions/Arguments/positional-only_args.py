# NOTE: positional-only arguments:
# can specify that a function can have ONLY positional args, or ONLY keyword args.
# are passed to a function in the order in which they are defined.
# add ', /' after the arguments:

# def your_mom(x, /):
#     print(x)

# your_mom(3)


# A bit of AI learnin':
# Example: the following function takes two positional arguments, 'name' and 'age':
def your_mom_2(name, age):
    print(f"Hello {name}! You are {age} years old.")

your_mom_2('Brad Balzak', 35)

# as you can see, the arguments are positioned in the same order that they would appear in the code/output


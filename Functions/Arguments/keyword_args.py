# NOTE: Keyword Arguments:
# are passed to a function by specifying the name of the argument.
# can send args w/ 'key = value' syntax - because of this, the order of args does not matter.


def the_function(lang3, lang2, lang1):
    print("The best language is " + lang2)

the_function(lang1 = "Perl", lang2 = "Python", lang3 = "Ruby")
print("\n")


# A secondary example:
def your_mom(name, age):
    print(f"Hello {name}! You are {age} years old.")

your_mom("Brad Balzak", 35)


# with keyword args, we are specifying the name of the argument.
# Keyword arguments can be useful for making our code more readable and maintainable - for example - if we have a function with many arguments, it can be helpful to pass the arguments by keyword so that it is clear what each argument is for. 


# Default Value:
# Keyword arguments can also be used to provide default values for arguments.
# For example, the following function takes keyword argument 'greeting' with default value of "Hello":

def your_mom_2(name, greeting='Hello'):
    print(f"{greeting}, {name}!")

your_mom_2('James')

# this function was called without passing a value for 'greeting' so the default value will be used
# NOTE: information can be passed into functions AS arguments.
# NOTE: args are specified after the function name, inside the parnethesis - you can add as many args as you want, separated by a commma.
 

# example of function w/one arg:
def a_function(fname):
    print(fname + " Chardonnay")

a_function("Tony")
a_function("Carl")
a_function("Paul")


print("\n")
# 'parameter' and 'argument' can be used interchangeably - data that's  passed into a function
# from a function's perspective: a parameter is the variable listed inside the parentheses in the function definition and an argument is the value that is sent to the function when it is called.



# NOTE: Number of Arguments:
# a fn must be called w/correct # of args - if fn expects 2 args, you must call w/2 args.

def name(fname, lname):
    print(f"{fname} {lname}")

name("James", "Price")
name("Jacque", "Dupont")
name("Curly", "Frogginbeard")
print("\n")



# NOTE: Arbitrary Arguments, *args:
# if an unknown amount of args is passed into your fn, add '*' before the parameter name in the fn definition:

def my_function(*cars):
    print("The fastest car is " + cars[2])
    
my_function("Mustang", "Chevelle", "Corvette")
print("\n")
# notice how args are basically in a list, and print statement in fn uses indexing to pick from args "kids[2]"



# NOTE: Keyword Arguments:
# send args w/key = value syntax - order of args does not matter this way.
def the_function(lang3, lang2, lang1):
    print("The best language is " + lang2)

the_function(lang1 = "Perl", lang2 = "Python", lang3 = "Ruby")
print("\n")



# NOTE: Arbitray Keyword Arguments - **kwargs
# if an unknown amount of keyword args will be passed into your fn, add two '**' asterisks before the parameter name in the function def.
# this way the fn will receive a dictionary of arguments, and can access the items accordingly: 

def das_function(**kwargs):
    print(f"His favorite language is " + kwargs["lang1"])
    
das_function(lang1 = "Python", lang2 = "Perl", lang3 = "Ruby")
print("\n")


# NOTE: Default Parameter Value
# calling a fn w/out an arg causes it to use the default value:
def an_function(lang = "Python"):
    print("I know " + lang)

an_function("Perl")
an_function("Ruby")
an_function()               # notice how it defaults to "Python" when no args passed
an_function("C++")
print("\n")



# NOTE: Passing a list as an argument: 
# any data types welcome when passing into a fn. - will be treated as same data type in fn. & output 

def passing_data(data):
    for x in data:
        print(x)

data = ["digital", "binary", "analog"]
passing_data(data)
print("\n")



# NOTE: Return Values:
# to let a fn return a value, use the return statement:
def b_function(x):
    return 5 * x

print(b_function(3))
print(b_function(5))
print(b_function(9))


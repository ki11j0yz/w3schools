# NOTE: Default Parameter Value
# calling a fn w/out an arg causes it to use the default value:
def an_function(lang = "Python"):
    print("I know " + lang)

an_function("Perl")
an_function("Ruby")
an_function()               # notice how it defaults to "Python" when no args passed
an_function("C++")
print("\n")
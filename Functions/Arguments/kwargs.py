# NOTE: Arbitray Keyword Arguments - **kwargs
# if an unknown amount of keyword args will be passed into your fn, add two '**' asterisks before the parameter name in the function def.
# this way the fn will receive a dictionary of arguments, and can access the items accordingly: 

def das_function(**kwargs):
    print(f"His favorite language is " + kwargs["lang1"])
    
das_function(lang1 = "Python", lang2 = "Perl", lang3 = "Ruby")
print("\n")
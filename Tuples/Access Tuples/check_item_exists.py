# use keyword: 'in' to specify an item present in a tuple:

tuple1 = ("car", "plane", "train", "bicycle", "boat")
query = input("What word would you like to search: ")

if query in tuple1:
    print("Yes, your query was found!")
else:
    print("No, your query was not found!")
    
# should output 'No'

# NOTE: I modified the program a smidge in order to allow a user to search for a certain word so that the program could output yes/no based on search query
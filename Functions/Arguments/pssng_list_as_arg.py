# NOTE: Passing a list as an argument: 
# any data types welcome when passing into a fn. - will be treated as same data type in fn. & output 

def passing_data(data):
    for x in data:
        print(x)

data = ["digital", "binary", "analog"]
passing_data(data)
print("\n")
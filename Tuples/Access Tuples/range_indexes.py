## You can specify a range of indexes by specifying the start/end point, such as [2:5] -> here the starting index is [2] and the ending index is [5]

tuple1 = ("Hawaii", "Arizona", "Utah", "Missouri", "Washington", "Delaware")
print(tuple1[2:5])
# outputs = ('Utah', 'Missouri', 'Washington')



## Leaving out the start value - range automatically starts with first index
print(tuple1[:3])

# of note: although the ending index is 3, the value "Missouri" is still omitted



## Leaving out the ending value - range automatically outputs until last index
print(tuple1[3:])



## Range of negative indexes: 
print(tuple1[-1:-3])
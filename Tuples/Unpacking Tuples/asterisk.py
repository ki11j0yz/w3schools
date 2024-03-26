# NOTE: If the # of variables is < # of values, you can add an '*' to the variable name and the values will be assigned to the variables as a list: 
states = ("Utah", "Arizona", "New Mexico", "Missouri", "Minnesota", "Kansas")

(obj1, obj2, *obj3) = states

print(obj1)
print(obj2)
print(obj3)


## NOTE: asterisk next to value other than last - Python will assign values to variable until # of values left matches # of variables left
(obj1, *obj2, obj3) = states

print(obj1)
print(obj2)
print(obj3)


### NOTE: notice in second iteration obj2 was the list until one last value remained to fill the obj3 variable

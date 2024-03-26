# NOTE: add()
set1 = {1, 2, 3}
set1.add(4)
print(set1)


# NOTE: clear() - removes all elements from a set: 
set2 = {1, 2, 3}
set2.clear()
print(set2)


# NOTE: copy() - returns a copy of the set:
set3 = {1, 2, 3}
set3 = set3.copy()
print(set3)     # NOTE: returns random order


# NOTE: difference() - returns a set containing the difference between two or more sets: 
set4 = {1, 2, 3}
set5 = {1, 2, "3"}
set4a = set4.difference(set5)
set5a = set5.difference(set4)
print(set4a)
print(set5a)
# NOTE: Notice the difference in outputs


# NOTE: difference_update() - removes items in a set that are also included in another:
set6 = {1, 2, 3, 4}
set7 = {1, 2, 5, 6}
set6.difference_update(set7)
print(set6)


# NOTE: isdisjoint() - returns whether two sets have an intersection or not: 
set8 = {1, 2, 3, 4}
set9 = {5, 6, 7, 8}
set8a = set8.isdisjoint(set9)       # NOTE: it seems the intersection is a difference
set9a = set9.isdisjoint(set8)
print(set8a)
print(set9a)

set10 = {1, 2, 3, 4}
set11 = {1, 2, 3, 4}                # NOTE: no difference or 'intersection' = 'False'
set10a = set10.isdisjoint(set11)
print(set10a)


# NOTE: issubset() - returns whether another set contains this set or not: 
set12 = {1, 2, 3, 4}
set13 = {5, 6, 7, 8}
set12a = set12.issubset(set13)
print(set12a)                               # False

set14 = {1, 2, 3, 4}                        # this set
set15 = {1, 2, 3, 4, 5, 6}                  # another set
set14a = set14.issubset(set15)
print(set14a)                               # True


# NOTE: issuperset() - returns whether this set contains another set or not: 
set16 = {1, 2, 3, 4, 5, 6, 7}               # this set
set17 = {1, 2, 3, 4}
set16a = set16.issuperset(set17)
print(set16a)                               # True

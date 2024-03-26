# NOTE: several ways to join sets: union(), update(), intersection_update(), intersection(), symmetric_difference(), symmetric_difference_update():


### union() method: returns new set containing all items from BOTH sets
cars = {"mustang", "chevelle", "trans-am"}
bands = {"whitesnake", "creed", "korn"}
combined_set = cars.union(bands)
print(combined_set)
# NOTE: both union() and update() will exclude duplicates in their output
6

### update() method - NOTE: inserts items in bands into cars:
cars.update(bands)
print(cars)


### intersection_update() method - NOTE: keeps ONLY the DUPLICATES:
set1 = {"IBM", "Apple", "Linux"}
set2 = {"Microsoft", "Apple", "Debian"}

set1.intersection_update(set2)
print(set1)


### intersection() method - NOTE: returns a new set that only contains items in both sets
set3 = {"Firefox", "Yahoo", "Google"}
set4 = {"Yahoo", "Duck-Duck-Go", "Brave"}
new_set = set3.intersection(set4)
print(new_set)


### symmetric_difference_update() - NOTE: keeps all items excluding duplicates
utensil = {"pen", "pencil", "hi-liter"}
writing = {"pencil", "fountain-pen", "mechanical-pencil"}
utensil.symmetric_difference_update(writing)
print(utensil)


### symmetric_difference() - NOTE: returns a new set with elements that are NOT in both sets:
new_set = {"apple", "google", "yahoo"}
second_set = {"apple", "google", "HP", "IBM"}
new_set = new_set.symmetric_difference(second_set)
print(new_set)

# NOTE: difference between symmetric_difference_update() and symmetric_difference() only varies by updating the calling set.
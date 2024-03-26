# NOTE: You can remove items from a set using the remove() or discard() methods:


### remove() method
set1 = {"key", "board", "micro", "bootstrap"}
set1.remove("micro")
print(set1)
# NOTE: if the item in remove() doesn't exist, Python will ERROR


### discard() method
set1.discard("board")
print(set1)
# NOTE: if item in set does not exist, discard() will NOT ERROR


### pop() method - will remove random item:
set1.pop()
print(set1)


### clear() method - empties entire set:
weights = {"5lb", "10lb", "25lb", "35lb"}
weights.clear()
print(weights)


### 'del' keyword - will delete set completely:
del weights
#print(weights)


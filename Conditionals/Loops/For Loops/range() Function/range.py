# NOTE: range() function helps us iterate through a set of code a specified # of times
# NOTE: returns a sequence of numbers, starting with 0 by default and increments by 1 (by default), and ends at a specified #:


# ye ol' print range() statement:
print(range(10))

# range() w/for loop
for z in range(10):
    print(z)
    
    
# parameters - starting at something other than 0 and incrementing wildly:
# syntax: range(start, end, step)
for z in range(0, 10, 2):
    print(z)

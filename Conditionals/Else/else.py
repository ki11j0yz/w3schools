# NOTE: 'else' keyword catches anything that might not be caught by the preceding conditions:

x = 5000
y = 5006
if y > x:
    print("y is greater than x")
elif x == y:
    print("x and y are equal")
else:
    print("x is greater than y")
    
    

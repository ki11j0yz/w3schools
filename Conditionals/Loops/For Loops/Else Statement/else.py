# NOTE: 'else' statement in 'for' loops - a specified block of code to be executed when the loop is finished:

# print numbers from <> to <> & print a message when the loop has ended:
for z in range(9):
    print(z)
else:
    print("Done")
    
    
    
# w/'break' statement:
# NOTE: 'else' block will NOT be executed if loop is stopped by a 'break'statement
for y in range(10):
    if y == 5:
        break
    print(y)
else:
    print("Done")
        
    
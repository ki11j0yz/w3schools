# NOTE: 'continue' statement - a loop control statement that tells the loop to skip the current iteration and move on the the next one. 
# NOTE: commonly used in 'for' loops, 'while' loops and 'do-while' loops.

# continue statement: 
for i in range(10):
    if i == 4:
        continue
    print(i)                # output will exclude int. 4
    
    
# in a 'while' loop:
i = 0
while i < 10:
    i += 1
    if i == 4:
        continue
    print(i)


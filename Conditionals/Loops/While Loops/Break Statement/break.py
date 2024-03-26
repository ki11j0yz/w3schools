# NOTE: 'break' statement is used to exit a loop prematurely - when execution reaches a break statement, the loop is immediately terminated and the program control resumes at the next statement following the loop.

# break statement:
for i in range(10):
    if i == 5:
        break
    print(i)
    
    
# with a 'while' loop:
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
print(i)            # added out of curiosity, even though loop ends at 4, i is == 5 which is where our break statement said "Bitch, stop. You 5 now."


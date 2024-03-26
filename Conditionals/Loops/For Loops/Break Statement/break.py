# NOTE: 'break' statement: as in 'while' loops, the 'break' statement is used to terminate a loop prematurely - when the break statement is encountered, the loop exits immediately and the program control resumes at the next statement.


# ye plain ol' for loop:
for i in range(10):
    if i == 5:
        break
    print(i)
    
# ye intermediate ol' for loop:
giants = ["Steve Wozniak", "Grace Hopper", "Ada Lovelace", "Alan Turing"]
for name in giants:
    if name == "Ada Lovelace":
        break
    print(name)         # will yield an output - try placing before 'if' statement
    

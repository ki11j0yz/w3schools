# NOTE: 'else' statement - allows you to execute a block of code if the condition in the if-statement is False:


# the primitive code:
name = str(input("Provide me with the correct name and I shall print your message: "))

if name == "Bob Thornton":
    print("Hello Bob Thornton, nice to meet you!")
else:
    print("Oh, Good-bye!")
    
    
# the boujie code:    
names = {
    "Gary McGonagle",
    "Chip Warnaby",
    "Sally Behemtep",
    "Elijah Gootherby"
}

name = str(input("Please provide the correct name and receive your message: "))

if name in names:
    print(f"Hello, you have 5 new top secret data briefs {name}")
else:
    print("You are not recognized, access denied.")
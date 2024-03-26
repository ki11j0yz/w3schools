# NOTE: To loop using a while loop, use the len() function to determine the length of the tuple, start a counter at 0 and then loop through index #'s - also remember to increase the counter after each iteration.
pokemon = ("Squirtle", "Pickachu", "Ekans", "Bulbasaur", "Dug-Trio", "Ghastly", "Meowth")
i = 0 
while i < len(pokemon):
    print(pokemon[i])
    i += 1
    
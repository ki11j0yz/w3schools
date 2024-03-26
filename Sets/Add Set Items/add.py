# NOTE: You can't change set items, but you can add them: 

### Add Items
set1 = {"car", "keyboard", "book", True}
set1.add("telephone")
print(set1)


### Add Sets - NOTE: to add another set into the current set use update():
nfc_set = {"Cardinals", "Falcons", "Panthers"}
afc_set = {"Chiefs", "Raiders", "Broncos"}
nfc_set.update(afc_set)
print(nfc_set)


### Add Any Iterable - NOTE: objecet in update() can be any iterable object (tuples, list, dict, etc.)
set2 = {"racket", "baseball bat", "hockey stick"}
sport = ["baseball", "basketball", "football"]
set2.update(sport)
print(set2)



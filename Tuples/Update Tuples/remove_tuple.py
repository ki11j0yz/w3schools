# NOTE: You can remove an item by converting to a list, using the '.remove', and then convert back to a tuple:

tuple1 = ("racing", "golf", "football", "soccer", "baseball", "hockey", "lacross")
print(tuple1)
x = list(tuple1)    # NOTE: tuple -> list conversion
x.remove("racing")
tuple1 = tuple(x)   # NOTE: list -> tuple conversion
print(tuple1)
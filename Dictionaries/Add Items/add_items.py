# NOTE: Bank of methods: update();
# NOTE: you can use a new index key and assign a new value to it when adding an item to a dictionary:

movie = {
    "Title": "Indiana Jones and Raiders of the Lost Ark",
    "Release Date": 1981,
    "Star": "Harrison Ford"
}
movie["Cameo"] = "Shia Lebouf"
print(movie)


# NOTE: update(): argument must be a dictionary, or an iterable object with key:value pairs:
movie.update({"cameo": "Sean Connery"})
print(movie)
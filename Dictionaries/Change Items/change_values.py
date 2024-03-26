# NOTE: Bank of methods: update();
# NOTE: specific values can be changed by referring to it's key name: 

# Referring to key name:

subway = {
    "12 inch?": "yes",
    "dressing?": "yes",
    "cookie?": "yes"
}
subway["cookie?"] = "no"
print(subway)


# NOTE: update(); argument must be a dictionary, or an iterable object with key:value pairs.

car = {
    "brand": "Chevy",
    "model": "Tahoe",
    "year": 2015
}
car.update({"year": 2024})
print(car)

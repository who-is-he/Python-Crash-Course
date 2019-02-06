import json

try:
    with open('number.json') as file_object:
        favorite_number = json.load(file_object)
except FileNotFoundError:
    print("There is no favorite number.")
else:
    print("I remember you. Your favorite number was " + favorite_number + ".")

input()
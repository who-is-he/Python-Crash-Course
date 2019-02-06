import json

try:
    with open('number.json') as file_object:
        favorite_number = json.load(file_object)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open('number.json', 'w') as file_object:
        json.dump(favorite_number, file_object)
        print("Your favorite number is " + favorite_number + "? I will remember that.")
else:
    print("I remember you. Your favorite number was " + favorite_number + ".")

input()
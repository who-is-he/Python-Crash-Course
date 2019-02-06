import json

favorite_number = input("What is your favorite number? ")
with open('number.json', 'w') as file_object:
    json.dump(favorite_number, file_object)
    print("Your favorite number is " + favorite_number + "? I will remember that.")

input()
first_name = input('what is your first name? ')
last_name = input('what is your last name? ')

with open('guest.txt', 'w') as file_object:
    file_object.write('logged: ' + first_name + ', ' + last_name)
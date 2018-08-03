with open('guest_list.txt', 'w') as file_object:
    file_object.write('guest book: ')

while True:
    first_name = input('guest first name: ')
    last_name = input('guest last name: ')

    if first_name == 'break' or last_name == 'break':
        break

    with open('guest_list.txt', 'a') as file_object:
        file_object.write('\n' + last_name + ', ' + first_name)
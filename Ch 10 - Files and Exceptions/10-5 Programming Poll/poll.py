with open('poll_results.txt', 'w') as file_object:
    file_object.write('poll results: ')

while True:
    name = input('what is your name? ')
    reason = input('why do you like programming? ')

    if name == 'break' or reason == 'break':
        break

    with open('poll_results.txt', 'a') as file_object:
        file_object.write('\n' + name + ': ' + reason)
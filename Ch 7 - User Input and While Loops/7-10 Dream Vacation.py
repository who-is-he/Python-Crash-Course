dream_vacation = {}
yesnt = ['yes', 'y', 'yeah', 'i do', 'yup', 'yuppers', 'yuhuh', 'yeeeup']

while True:
    name = input('hello, what is your first name? ')
    vacation = input('hey ' + name + ', where would you like to go on vacation? ')
    answer = input('you want to go to ' + vacation + '? thats awesome. do you know anyone else that would like to poll? ')
    dream_vacation[name] = vacation

    if answer in yesnt:
        print('cool')
    else:
        print('thanks for your input')
        break

for name, destination in dream_vacation.items():
    print(name + ' wanted to go to ' + destination)

input()

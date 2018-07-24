while True:
    age = input('what is your age? ')
    age = int(age)

    if age < 3:
        print('your ticket is free')
    elif age < 12:
        print('the price of your ticket is $10')
    else: 
        print('the price of your ticket is $15')
    print()
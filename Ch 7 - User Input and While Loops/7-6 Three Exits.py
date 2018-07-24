while True:
    topping = input('please enter a pizza topping of your choice \ntype \'nothing\' for a plain pizza:\n')
    if topping != 'nothing':
        print('adding ' + topping + ' to your pizza')
    else:
        print('adding NOTHING to your pizza. enjoy')
        break

ordering = True
while ordering:
    topping = input('please enter a pizza topping of your choice \ntype \'stop\' if you\'d like to stop ordering a pizza:\n')
    if topping != 'stop':
        print('adding ' + topping + ' to your pizza')
    else:
        ordering = False
        print('wow that\'s a lot of toppings')

toppings = 0

while toppings < 3:
    topping = input('please enter a pizza topping of your choice: ')
    print('adding ' + topping)
    toppings += 1

print('ordering a pizza with ' + toppings + ' toppings.')
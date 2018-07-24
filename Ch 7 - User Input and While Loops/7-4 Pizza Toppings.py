while True:
    topping = input('please enter a pizza topping of your choice \ntype \'order\' to order your pizza\n')
    if topping != 'order':
        print('adding ' + topping + ' to your pizza')
    else:
        print('goodbye')
        break
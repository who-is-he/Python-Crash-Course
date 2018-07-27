def request_toppings(*toppings):
    str = 'making a sandwich with the following toppings: '
    for topping in toppings:
        str += '-' + topping + ' '
    print(str)

request_toppings('ham', 'cheese', 'lettuce')
request_toppings('bacon', 'lettuce', 'tomato', 'mayo')
request_toppings('tuna', 'american cheese', 'onions', 'pepper', 'lettuce')
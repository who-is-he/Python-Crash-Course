sandwich_orders = ['gyro', 'hero', 'pastrami', 'cuban', 'pastrami', 'turkey', 'pastrami', 'ham', 'club']
finished_sandwiches = []
print(str(sandwich_orders).replace('\'','')[1:-1] + ' have all been requested')
print('we are out of pastrami!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('making a fresh ' + sandwich + ' sandwich')
    finished_sandwiches.append(sandwich)

print('i\'ve made these sandwiches: ' + str(finished_sandwiches).replace('\'','')[1:-1])
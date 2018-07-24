sandwich_orders = ['gyro', 'hero', 'cuban', 'turkey', 'ham', 'club']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('making a fresh ' + sandwich + ' sandwich')
    finished_sandwiches.append(sandwich)

print('i\'ve made these sandwiches: ' + str(finished_sandwiches).replace('\'','')[1:-1])
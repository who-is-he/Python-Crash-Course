#Animals
animals = ['Dogs', 'Cats', 'Birds']

for animal in animals:
    print(animal+" would make great pets!")

print('All of these animals are common household pets!')

#My Pizzas, Your Pizzas
pizzas = ['Cheese','Pepperoni','Meatlover']
friend_pizzas = pizzas[:]
friend_pizzas.append('Hawaiian')

print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza)

print('My friend\'s favorite pizzas are: ')
for pizza in friend_pizzas:
    print(pizza)

#More Loops
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print('My favorite foods are:')
for food in my_foods:
    print(food)

print('\nMy friend\'s favorite foods are:')
for food in friend_foods:
    print(food)
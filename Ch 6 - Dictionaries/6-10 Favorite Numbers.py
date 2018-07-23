favorite_numbers = {
    'mike': [1, 2],
    'alex': [1, 2, 3],
    'isabella': [2, 3, 4],
    'jordan': [3, 4, 5]
}

for person, numbers in favorite_numbers.items():
    print(person + ' likes the numbers ' + str(numbers).replace('\'','')[1:-1])
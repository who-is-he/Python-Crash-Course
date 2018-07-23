import random

favorite_numbers = {
    'mike': [random.randint(1, 20) for x in range(random.randint(1, 5))],
    'alex': [random.randint(1, 20) for x in range(random.randint(1, 5))],
    'isabella': [random.randint(1, 20) for x in range(random.randint(1, 5))],
    'jordan': [random.randint(1, 20) for x in range(random.randint(1, 5))]
}

total_numbers = []

for numbers in favorite_numbers.values():
    print(numbers)
    total_numbers = set(total_numbers) | set(numbers)

print('favorite numbers included: ' + str(total_numbers)[1:-1])
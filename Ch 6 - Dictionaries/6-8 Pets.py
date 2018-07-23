pets = []

sparky = {
    'name': 'sparky',
    'owner': 'stacy',
    'type': 'dog',
    'color': 'b/w',
    'size:': 'small'
}
pets.append(sparky)

mango = {
    'name': 'mango',
    'owner': 'bill',
    'type': 'cat',
    'color': 'orange',
    'size:': 'medium'
}
pets.append(mango)

tango = {
    'name': 'tango',
    'owner': 'mango',
    'type': 'cat',
    'color': 'light orange',
    'size:': 'big'
}
pets.append(sparky)

coco = {
    'name': 'coco',
    'owner': 'alex',
    'type': 'cat',
    'color': 'white',
    'size': 'tiny'
}
pets.append(coco)

for pet in pets:
    for key, value in pet.items():
        print(key + ': ' + value)
    print()
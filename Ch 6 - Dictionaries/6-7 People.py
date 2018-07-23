people = []

person1 = {
    'first_name': 'Mike',
    'last_name': 'Evans',
    'age': 18,
    'city': 'Tampa'
}
people.append(person1)

person2 = {
    'first_name': 'Jordan',
    'last_name': 'McMillan',
    'age': 17,
    'city': 'Tampa'
}
people.append(person2)

person3 = {
    'first_name': 'Isabella',
    'last_name': 'Alfonso',
    'age': 18,
    'city': 'Tampa',
}
people.append(person3)

for person in people:
    for info, value in person.items():
        print(info + ": " + str(value))
    print()
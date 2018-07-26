magicians = ['mike', 'alex', 'jordan']

def make_great(magicians):
    great_magicians = []

    while magicians:
        great_magicians.append(magicians.pop() + ' the great')

    for great_magician in great_magicians:
        magicians.append(great_magician)

def show_magicians(magicians):
    for magician in magicians:
        print(magician + ' is a magician')

make_great(magicians)
show_magicians(magicians)
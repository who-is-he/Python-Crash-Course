magicians = ['mike', 'alex', 'jordan']

def make_great(magicians):
    great_magicians = []

    while magicians:
        great_magicians.append(magicians.pop() + ' the great')

    return great_magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician + ' is a magician')

show_magicians(make_great(magicians[:]))
show_magicians(magicians)
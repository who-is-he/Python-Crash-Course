def print_lines(filename):
    try:
        with open(filename) as file_object:
            print(file_object.read())
    except FileNotFoundError:
        pass

print_lines('dogs.txt')
print_lines('cat.txt')
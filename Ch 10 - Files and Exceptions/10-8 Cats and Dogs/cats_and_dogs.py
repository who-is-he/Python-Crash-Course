def print_lines(filename):
    try:
        with open(filename) as file_object:
            print(file_object.read())
    except FileNotFoundError:
        print("Could not find '" + filename + "'.")

print_lines('dogs.txt')
print_lines('cat.txt')
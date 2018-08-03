with open('learning_python.txt') as file_object:
    print(file_object.read().replace('python', 'lua'))

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.strip().replace('python', 'lua'))

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip().replace('python', 'lua'))
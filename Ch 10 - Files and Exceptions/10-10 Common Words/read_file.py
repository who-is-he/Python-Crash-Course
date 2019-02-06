def parse_file(filename):
    num_lines = sum(1 for line in open(filename))

    with open(filename) as file_object:
        the_count = 0
        for line in file_object:
            the_count += line.lower().count('the')

        return(filename + " contains " + str(num_lines) + " lines and " 
            + str(the_count) + " uses of the word 'the'.")

print(parse_file('moby_dick.txt'))
print(parse_file('pride_and_prejudice.txt'))
print(parse_file('the_iliad_of_homer.txt'))

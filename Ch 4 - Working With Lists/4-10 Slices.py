numbers = [value for value in range(1,1000001)]

print('The first three items in the list are: '+' '.join(str(n) for n in numbers[0:3]))
print('Three items from the middle of the list are: '+' '.join(str(n) for n in numbers[len(numbers)//2:len(numbers)//2+3]))
print('The last three items in the list are '+' '.join(str(n) for n in numbers[-3:]))
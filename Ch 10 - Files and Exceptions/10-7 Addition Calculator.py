print("Type two numbers to add them together.")

while True:
    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")

    if n1 == "break" or n2 == "break":
        break

    try:
        sum = int(n1) + int(n2) 
    except ValueError:
        print("Please enter valid numbers.")
    else:
        print(n1 + " + " + n2 + " = " + str(sum))
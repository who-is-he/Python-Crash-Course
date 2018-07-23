boolean1 = False
boolean2 = not boolean1
age1 = 10
age2 = 20
lizt1 = ['a', 'b', 'c']
string1 = 'hello world'
string2 = 'hello'
string3 = 'world'
lizt2 = [age1, age2, lizt1, string1, string2, string3]
lizt3 = ['A', 'B', 'C']
lizt4 = lizt1.reverse()

print('False: ')
print(boolean1 == boolean2) #false
print(age1 >= age2 and True) #false
print(string1 == string2+string3) #false
print(lizt4 == lizt1) #false
print(lizt2[1] == age1) #false

print('\nTrue: ')
print(age1 <= age2 and True) #true
print(lizt1 in lizt2) #true
print(string1 == string2 + ' ' + string3) #true
print(lizt3[1].lower() in lizt1) #true
print(boolean1 or boolean2) #true
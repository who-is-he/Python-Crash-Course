guests = ['Leonhard Euler', 'Alfred Einstein', 'Karl Marx']
print(guests[0]+', I invite you to dinner to teach me maths.\n'+guests[1]+', I invite you to dinner to teach me Physics.\n'+guests[2]+', I invite you to dinner to spread class consciousness.')
print('It looks like '+guests[0]+' got stuck in traffic and couldn\'t make it.')
guests[0] = 'Isaac Newton'
print('My buddy '+guests[0]+' could teach me instead!')
print('This just in! We have a new table that can hold three more people.')
guests.insert(0, 'John')
guests.insert(len(guests)//2,'Jane')
guests.append('Bob')
print(guests[0]+', you are formally invited to my dinner party!')
print(guests[1]+', you are formally invited to my dinner party!')
print(guests[2]+', you are formally invited to my dinner party!')
print(guests[3]+', you are formally invited to my dinner party!')
print(guests[4]+', you are formally invited to my dinner party!')
print(guests[5]+', you are formally invited to my dinner party!')
print('Uh oh, our table won\'t be in in time for dinner! I can only have two guests!')
print(guests.pop()+', sorry! You won\'t be able to come!')
print(guests.pop()+', sorry! You won\'t be able to come!')
print(guests.pop()+', sorry! You won\'t be able to come!')
print(guests.pop()+', sorry! You won\'t be able to come!')
del guests[0]
del guests[0]
print(guests)
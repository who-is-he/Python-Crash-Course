buffet = ('chicken','potatoes','gravy','ham','corn')
for food in buffet:
	print(food)

#buffet[0] = 'turkey' TypeError: 'tuple' object does not support item assignment

buffet = ('chicken','potatoes','gravy','turkey','green beans')
for food in buffet:
	print(food)
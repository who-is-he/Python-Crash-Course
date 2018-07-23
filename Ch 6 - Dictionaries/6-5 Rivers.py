rivers = {
	'mississippi': 'mississippi',
	'europe': 'danube',
	'india': 'ganges'
}

for zone, river in rivers.items():
	print('the ' + river + ' river runs through '+zone)

for zone in rivers:
	print(zone)

for river in rivers.values():
	print(river)
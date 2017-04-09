places = ['Colorado','Chicago','Quebec','Toronto','Portland','Japan','United Kingdom','New Mexico']
print(places)
print(sorted(places))
print(sorted(places,reverse=True))
places.reverse()
places.insert(len(places)//2,'Maine')
places.reverse()
places.sort()
places.sort(reverse=True)
places.remove('Japan')
print(places.pop(2))
del places[-1]
places.append('China')
print(places)
favorite_places = {
    'ryan': ['washington', 'new york', 'maine'],
    'grant': ['texas', 'colorado'],
    'grace': ['colorado', 'california', 'oregon']
}

for person, places in favorite_places.items():
    print(person + ' likes to visit ' + str(places).replace('\'','')[1:-1])
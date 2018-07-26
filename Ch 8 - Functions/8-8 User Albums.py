def make_album(artist, album):
    return {'artist': artist, 'album': album}

print('input an artist name and their best album. type q to quit at any time')

while True:
    artist = input('artist name: ')
    if artist == 'q':
        break

    album = input('artist album: ')
    if album == 'q':
        break

    print(make_album(artist, album))
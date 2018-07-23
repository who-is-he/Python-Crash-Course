favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

to_be_polled = ['mike', 'sarah', 'greg', 'phil', 'jay']

for name in to_be_polled:
    if name in favorite_languages:
        print('thanks for taking the poll, ' + name)
    else:
        print('hey ' + name + ', please take the poll')

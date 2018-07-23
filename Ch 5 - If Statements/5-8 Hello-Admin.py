usernames = ['person', 'player', 'who is he', 'unadmin', 'admin']

for username in usernames:
	if username == 'admin':
		print('welcome back, admin, would you like to see a status report?')
	else:
		print('welcome back, ' + username)
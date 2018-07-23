usernames = ['person', 'player', 'who is he', 'unadmin', 'admin']
new_users = ['person229', 'ADMIN', 'quest', 'player', 'greg']
current_users_lower = [user.lower() for user in usernames]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(new_user + ' already in use. please choose another.')
	else:
		print(new_user + ' is available.')
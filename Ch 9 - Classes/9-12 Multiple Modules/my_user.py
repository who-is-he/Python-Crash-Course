from admin import Admin

user1 = Admin('mike', 'evans', age=18, country='us')
user1.greet_user()
user1.privileges.show_privileges()

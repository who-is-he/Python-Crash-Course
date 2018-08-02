class User():
    def __init__(self, first_name, last_name, **info):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
        for k, v in info.items():
            setattr(self, k, v)

    def describe_user(self):
        for attr, value in self.__dict__.items():
            print(str(attr) + ': ' + str(value))

    def greet_user(self):
        print('\nhello ' + self.first_name.title() + ' ' 
            + self.last_name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, **info):
        super().__init__(first_name, last_name, **info)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ['add post', 'delete post', 'edit', 'ban', 'kick', 'warn']

    def show_privileges(self):
        print('user can: ' 
            + str(self.privileges[0:-1]).replace('\'','')[1:-1] + ', and '+
            self.privileges[-1])

user1 = Admin('mike', 'evans', age=18, country='us')
user1.privileges.show_privileges()
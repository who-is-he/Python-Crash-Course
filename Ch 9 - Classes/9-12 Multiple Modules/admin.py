from user import User

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

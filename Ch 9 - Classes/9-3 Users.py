class User():
    def __init__(self, first_name, last_name, **info):
        self.first_name = first_name
        self.last_name = last_name
        
        for k, v in info.items():
            setattr(self, k, v)

    def describe_user(self):
        for attr, value in self.__dict__.items():
            print(str(attr) + ': ' + str(value))

    def greet_user(self):
        print('\nhello ' + self.first_name.title() + ' ' 
            + self.last_name.title() + '!')

user1 = User('mike', 'evans', age=18)
user1.greet_user()
user1.describe_user()

user2 = User('ashton', 'johnson', age=22, height='5\'10', weight='143 lbs')
user2.greet_user()
user2.describe_user()

user3 = User('rickie', 'bisnath')
user3.greet_user()
user3.describe_user()
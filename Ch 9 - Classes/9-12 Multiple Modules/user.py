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
        print('hello ' + self.first_name.title() + ' ' 
            + self.last_name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

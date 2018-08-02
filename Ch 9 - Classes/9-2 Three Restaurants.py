class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' serves exclusively ' 
            + self.cuisine_type.title() + ' cuisine')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open!')

restaurant1 = Restaurant('olive garden', 'italian')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('moes', 'mexican')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('jets', 'pizza')
restaurant3.describe_restaurant()
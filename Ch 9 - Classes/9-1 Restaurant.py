class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' serves exclusively ' 
            + self.cuisine_type.title() + ' cuisine')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open!')

restaurant = Restaurant('olive garden', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
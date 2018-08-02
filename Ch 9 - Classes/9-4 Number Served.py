class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' serves exclusively ' 
            + self.cuisine_type.title() + ' cuisine')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open!')

    def set_number_served(self, n):
        self.number_served = n

    def increment_number_served(self, n):
        self.set_number_served(self.number_served + n)

    def print_number_served(self):
        print(self.restaurant_name.title() + ' has served ' 
            + str(self.number_served) + ' people')

restaurant = Restaurant('olive garden', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.increment_number_served(10)
restaurant.print_number_served()
restaurant.increment_number_served(15)
restaurant.print_number_served()
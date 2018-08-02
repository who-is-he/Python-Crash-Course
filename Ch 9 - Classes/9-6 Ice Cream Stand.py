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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_flavors(self):
        print(self.restaurant_name.title() + ' serves the flavors: '
            + str(self.flavors[0:-1]).replace('\'','')[1:-1] + ', and '+
            self.flavors[-1])

nIce = IceCreamStand('nIce', 'ice cream', 
    ['chocolate', 'vanilla', 'caramel', 'strawberry', 'mint', 'coffee'])
nIce.open_restaurant()
nIce.describe_restaurant()
nIce.describe_flavors()
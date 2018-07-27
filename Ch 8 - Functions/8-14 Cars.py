def make_car(manufacturer, model_name, **info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name

    for k, v in info.items():
        car[k] = v

    return car

car_1 = make_car('ford', 'focus', year=2014, color='white', owner_name='mike evans')
print(car_1)
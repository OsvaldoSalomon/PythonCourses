class Vehicle:
    # This variable should not be changed outside of the class specification
    # This is a class attribute
    vehicle_counter = 0

    def __init__(self, body_type, make):
        self.vehicle_body = body_type
        self.vehicle_make = make
        Vehicle.vehicle_counter += 1

    def get_vehicle_count(self):
        return Vehicle.vehicle_counter


car1 = Vehicle("Avanza", "Toyota")
print(car1)
print(car1.vehicle_body)
print(car1.vehicle_make)
print(type(car1))

car2 = Vehicle("Truck", "Mercedes")
car3 = Vehicle("Sedan", "Toyota")
car4 = Vehicle("Sport", "Mercedes")
car5 = Vehicle("Motorcycle", "Mercedes")
car6 = Vehicle("Sedan", "Honda")

print(car1.get_vehicle_count())

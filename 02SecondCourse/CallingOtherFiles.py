from machines.vehicle_stuff import Vehicle, Truck, Motorcycle

truck1 = Truck("Big Rig", "Mercedes")
car1 = Vehicle("Sedan", "Chevrolet")
moto1 = Motorcycle("Sports", "Honda")

# print(truck1.get_vehicle_count())
# truck1.drive()

for v in [truck1, car1, moto1]:
    v.drive()


def perform_tasks(vehicle_object):
    vehicle_object.drive()


perform_tasks(truck1)

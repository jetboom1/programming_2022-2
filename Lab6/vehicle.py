class Vehicle:
    def __init__(self, firm, model, type, volume=0, consumption=0, fuel_level=0):
        self.firm = firm
        self.model = model
        self.type = type
        self.gas_tank_size = volume
        self.consumption = consumption
        self.fuel_level = fuel_level
    def __repr__(self):
        return f"Vehicle {self.firm} {self.model} is a {self.type}. It has a gas tank size of {self.gas_tank_size}."
    def fuel_up(self, amount):
        self.fuel_level += amount
        if self.fuel_level > self.gas_tank_size:
            self.fuel_level = self.gas_tank_size
            return 'Gas tank is fully filled.'
        return 'Gas tank is filled.'
    def drive(self, distance):
        if self.fuel_level < self.consumption * distance / 100:
            return "Not enough fuel level in a gas tank."
        else:
            self.fuel_level -= self.consumption*distance/100
            return f"The {self.firm} {self.model} is now driving."
    def get_fuel_level(self):
        return self.fuel_level


class Battery:
    def __init__(self, capacity=85, charge_level=0):
        self.size = capacity
        self.charge_level = charge_level


class ElectricVehicle(Vehicle):
    def __init__(self, firm, model, type):
        super(ElectricVehicle, self).__init__(firm, model, type, 0, 0, 0)
        self.battery = Battery()
    def charge(self, amount=100):
        self.battery.charge_level += amount
        if self.battery.charge_level >=а 100:
            self.battery.charge_level = 100
            return "The vehicle is fully charged."
        return 'The vehicle is charged.'
    def __str__(self):
        return f"Vehicle {self.firm} {self.model} is a {self.type}."
    def drive(self, distance=0):
        self.battery.charge_level = 0
        return f"The {self.firm} {self.model} is now driving."
    def get_charge_level(self):
        return self.battery.charge_level
    def get_battery_info(self):
        return f"Battery has size of {self.battery.size}, it is charged up to {self.battery.charge_level}%"


def test_vehicle():
    """
    Test function
    """
    print("Testing Vehicle classes...")
    # A basic Vehicle has a brand, model, type, volume of gas_tank_size
    # fuel_level that by default equals 0 and fuel_consumption
    # that by default equals 6. It can drive and be fueled up
    vehicle = Vehicle("Subaru", "Forester", "Crossover", 16, 7)
    assert (type(vehicle) == Vehicle)
    assert (isinstance(vehicle, Vehicle))
    assert (str(vehicle) == "Vehicle Subaru Forester is a Crossover. It has a gas tank size of 16.")

    # change some attributes
    assert (vehicle.fuel_up(12) == "Gas tank is filled.")
    assert (vehicle.get_fuel_level() == 12)
    # When vehicle drives, it uses the fuel level
    # Vehicle uses fuel in amount of
    # fuel_consumption * distance to drive / 100
    assert (vehicle.drive(100) == "The Subaru Forester is now driving.")
    # the vehicle travelled 100 km and the fuel level reduced
    # from 12 to 5
    assert (vehicle.get_fuel_level() == 5)
    assert (vehicle.drive(100) == "Not enough fuel level in a gas tank.")

    # ElectricVehicle is a Vehicle that doesn't need a gas_tank_size
    # and doesn't have a fuel_consumption.
    # You can charge and drive it.
    electric_vehicle = ElectricVehicle('Tesla', 'Model 3', 'Sedan')
    assert (type(electric_vehicle) == ElectricVehicle)
    assert (isinstance(electric_vehicle, ElectricVehicle))
    assert (isinstance(electric_vehicle, Vehicle))
    assert (str(electric_vehicle) == "Vehicle Tesla Model 3 is a Sedan.")

    assert (electric_vehicle.get_fuel_level() == 0)
    assert (electric_vehicle.charge() == "The vehicle is fully charged.")
    assert (electric_vehicle.get_charge_level() == 100)
    assert (electric_vehicle.drive() == "The Tesla Model 3 is now driving.")
    assert (electric_vehicle.get_charge_level() == 0)

    # the attribute battery has to belong to Battery class
    # the Battery has a size, that by default equals 85
    # and charge level that by default equals 0
    assert (type(electric_vehicle.battery) == Battery)
    assert (isinstance(electric_vehicle.battery, Battery))
    assert (electric_vehicle.get_battery_info() == "Battery has size of 85, it is charged up to 0%")

    print("Done!")


if __name__ == '__main__':
    test_vehicle()
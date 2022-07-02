orderId = 0


class Location:
    def __init__(self, city: str, postoffice: int):
        self.city = city
        self.postoffice = postoffice


class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Vehicle:
    def __init__(self, vehicleNo: int):
        self.vehicleNo = vehicleNo
        self.isAvailable = True


class Order:
    def __init__(self, user_name: str, city, postoffice, items):
        global orderId
        orderId += 1
        self.orderId = orderId
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = None

    def __str__(self):
        return f'Your order number is {self.orderId}'

    def calculateAmount(self) -> int:
        """This function calculates and returns the total value of goods sent"""
        sum = 0
        for item in self.items:
            sum += item.price
        return sum

    def assignVehicle(self, vehicle: Vehicle) -> None:
        """this function assigns vehicle to an order"""
        self.vehicle = vehicle


class LogisticSystem:
    '''The dispatcher of the orders'''
    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.sent_orders = []

    def placeOrder(self, order: Order) -> None or str:
        """if there is available vehicle, sents the order"""
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                order.assignVehicle(vehicle)
                self.sent_orders.append(order)
                vehicle.isAvailable = False
                return None
        print('There is no available vehicle to deliver an order.')

    def trackOrder(self, order_id):
        """Returns the current status of the order"""
        for order in self.sent_orders:
            if order_id == order.orderId:
                print(f'Your order #{order_id} is sent to {order.location.city}. Total price: ' \
                       f'{order.calculateAmount()} UAH.')
                return True
        print('No such order')
        return False


if __name__ == '__main__':
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item('book', 110), Item('chupachups', 44)]
    my_order = Order(user_name='Oleg', city='Lviv', postoffice=53, items=my_items)
    print(my_order)
    logSystem.placeOrder(my_order)
    logSystem.trackOrder(my_order.orderId)

    my_items2 = [Item('flowers', 11), Item('shoes', 153), Item('helicopter', 0.33)]
    my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    print(my_order2)
    logSystem.placeOrder(my_order2)
    logSystem.trackOrder(my_order2.orderId)

    my_items3 = [Item('coat', 61.8), Item('shower', 5070), Item('rollers', 700)]
    my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    print(my_order3)
    logSystem.placeOrder(my_order3)
    logSystem.trackOrder(my_order3.orderId)


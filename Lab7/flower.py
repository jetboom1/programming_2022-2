class Flower:
    def __init__(self, name, color, petal, price):
        self.name = name
        self.color = color
        self.petal = petal
        self.price = price
        self.check_name()
        self.check_color()
        self.check_petal()
        self.check_price()

    def check_name(self):
        if type(self.name) != str:
            raise AttributeError("Name is not a string")

    def check_color(self):
        if type(self.color) != str:
            raise AttributeError("Color is not a string")

    def check_petal(self):
        if type(self.petal) != int or self.petal < 0:
            raise AttributeError("Petal is not an integer or negative")

    def check_price(self):
        if type(self.price) != int or self.price < 0:
            raise AttributeError("Price is not an integer or negative")

    def __str__(self):
        return f"{self.name} {self.color} {self.petal}"


class Tulip(Flower):
    def __init__(self, petal, price):
        super().__init__('Tulip', 'pink', petal, price)

class Rose(Flower):
    def __init__(self, petal, price):
        super().__init__('Rose', 'red', petal, price)

class Chamomile(Flower):
    def __init__(self, petal, price):
        super().__init__('Chamomile', 'white', petal, price)

class FlowerSet():
    def __init__(self):
        self.flowers = []
        self.set_class = [Flower, Tulip, Rose, Chamomile]

    def __str__(self):
        return f"Number of flowers in set: {len(self.flowers)}"

    def add_flowers(self, flower):
        for flow in self.flowers:
            self.set_class = flow.__class__
        if not isinstance(flower, Flower):
            raise AttributeError("flower is not a Flower class instance")
        if flower.__class__ == self.set_class:
            self.flowers.append(flower)
        elif not self.flowers:
            self.flowers.append(flower)
        else:
            raise AttributeError("Flower is not the same type of flowers in the set")

class Bucket():
    def __init__(self):
        self.sets = []

    def __str__(self):
        return f"Number of sets in bucket: {len(self.sets)}"

    def add_set(self, set):
        if not isinstance(set, FlowerSet):
            raise AttributeError("given value is not a FlowerSet class instance")
        self.sets.append(set)

    def total_price(self):
        sum = 0
        for set in self.sets:
            for flower in set.flowers:
                sum += flower.price
        return sum


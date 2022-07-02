class Markets:
    def __init__(self, name, area, categories):
        self.name = name
        self.area = area
        self.categories = categories
    def __str__(self):
        return f'Supermarket {self.name} has an area of {self.area} m2 and has the following categories: ' \
               f'{", ".join(self.categories)}.'

market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy', 'Beverages'])
print(market_family_food)

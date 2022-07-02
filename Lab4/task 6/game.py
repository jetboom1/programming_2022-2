class Street:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.rooms = {'north': None, 'west': None,'south': None,'east': None}
        self.character = None
        self.item = None
    def set_description(self, desc):
        self.description = desc
    def set_character(self, char):
        self.character = char
    def set_item(self, item):
        self.item = item
    def link_room(self, base_room, direction):
        base_room.rooms[direction] = self
    def get_character(self):
        return self.character
    def get_details(self):
        print(self.name)
        print('--------------')
        print(self.description)
        for key in self.rooms.keys():
            if self.rooms[key]:
                print(f'{self.rooms[key].name} is {key}')
    def get_item(self):
        return self.item
    def move(self, direction):
        return self.rooms[direction]

class Enemy:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None
    def set_conversation(self, conv):
        self.conversation = conv
    def set_weakness(self, item_name):
        self.weakness = item_name
    def describe(self):
        print(self.description)
    def talk(self):
        print(self.conversation)
    def fight(self, item):
        if self.weakness == item:
            return True
        return False

class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, desc):
        self.description = desc

    def describe(self):
        print(f'The {self.name} is here - {self.description}')

    def get_name(self):
        return self.name




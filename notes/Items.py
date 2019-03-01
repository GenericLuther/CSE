class Item(object):
    def __init__(self, name):
        self.name = name

class Consumable(Item):
    def __init__(self):
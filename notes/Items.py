class Item(object):
    def __init__(self, name):
        self.name = name

class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)
        self.name = name
class Potion(Consumable):
    def __init__(self, name, heal, buff, debuff ):
        super(Potion, self).__init__(name)
        heal = heal
        buff = buff
        debuff = debuff
class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)

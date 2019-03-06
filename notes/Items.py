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
        self.heal = heal
        self.buff = buff
        self.debuff = debuff


class Food(Consumable):
    def __init__(self, name, hunger, heal, buff, debuff):
        super(Food, self).__init__(name)
        self.hunger = hunger
        self.heal = heal
        self.buff = buff
        self.debuff = debuff


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)


class Sword(Weapon):
    def __init__(self, name, durability, damage, ability):
        super(Sword, self).__init__(name)
        self.durability = durability
        self.damage = damage
        self.ability = ability


class Shield(Weapon):
    def __init__(self, name, durability, damage, ability):
        super(Shield, self).__init__(name)
        self.durability = durability
        self.damage = damage
        self.ability = ability


class Demonitizer(Weapon):
    def __init__(self, name, ammo, damage, ability):
        super(Demonitizer, self).__init__(name)
        self.ammo = ammo
        self.damage = damage
        self.ability = ability


class Throwable(Weapon):
    def __init__(self, name, ammo, damage, ability):
        super(Throwable, self).__init__(name)
        self.ammo = ammo
        self.damage = damage
        self.ability = ability


class Clothing(Item):
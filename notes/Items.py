class Ability(object):
    def __init__(self, name):
        self.name = name


class Fire(Ability):
    def __init__(self, name, fire):
        super(Fire, self).__init__(name)
        


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
    def __init__(self, name, protection, durability, damage, ability):
        super(Shield, self).__init__(name)
        self.protection = protection
        self.durability = durability
        self.damage = damage
        self.ability = ability


class Demonitizer(Weapon):
    def __init__(self, name, ammo, accuracy, damage, ability):
        super(Demonitizer, self).__init__(name)
        self.ammo = ammo
        self.range = accuracy
        self.damage = damage
        self.ability = ability


class Throwable(Weapon):
    def __init__(self, name, ammo, damage, ability):
        super(Throwable, self).__init__(name)
        self.ammo = ammo
        self.damage = damage
        self.ability = ability


class Clothing(Item):
    def __init__(self, name):
        super(Clothing, self).__init__(name)


class ChestPlate(Clothing):
    def __init__(self, name, protection, durability, flexibility):
        super(ChestPlate, self).__init__(name)
        self.protection = protection
        self.durability = durability
        self. flexibility = flexibility


class Shoes(Clothing):
    def __init__(self, name, speed, durability, jump, grip):
        super(Shoes, self).__init__(name)
        self.speed = speed
        self. durability = durability
        self.jump = jump
        self.grip = grip


class Leggings(Clothing):
    def __init__(self, name, protection, durability, space, flexibility):
        super(Leggings, self).__init__(name)
        self. protection = protection
        self.durability = durability
        self.space = space
        self. flexability = flexibility
"""
class Helmet(Clothing):
    def __init__(self, name, fast_travel):
        super(Helmet, self).__init__(name)
"""


class Boom_Boom(Demonitizer):
    def __init__(self):super(Boom_Boom, self).__init__('BoomBoom', 10, .5, 50, None)


players_BOOMBOOM = Boom_Boom


class Character(object):
    def __init__(self, name: str, health: int, weapon, clothes):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.clothes = clothes

    def take_damage(self, damage: int):
        if self.clothes is None:
            self.health -= damage
        else:
            self.health -= damage * self.clothes.protection
        print("%s had %d left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


sword = Sword("Sword", 100, 20, None)
gold_chestplate = ChestPlate("Golden ChestPlate", .80, 70, None)

skeleton = Character("Skelly Boy", 120, sword, gold_chestplate)
blubber_boy = Character("Blubber Boy", 250, sword, None)
skeleton.attack(blubber_boy)
blubber_boy.attack(skeleton)
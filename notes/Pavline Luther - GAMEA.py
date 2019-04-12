

# Items
class Item(object):
    def __init__(self, name):
        self.name = name


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)


class Potion(Consumable):
    def __init__(self, name, heal, buff, debuff, amount):
        super(Potion, self).__init__(name)
        self.heal = heal
        self.buff = buff
        self.debuff = debuff
        self.hunger = 0
        self.amount = amount

    def consume(self):
        self.amount -= 1
        print("You gained %s health" % self.heal)


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
    def __init__(self, name, durability, damage, penetration, ability):
        super(Sword, self).__init__(name)
        self.durability = durability
        self.damage = damage
        self.penetration = penetration
        self.ability = ability


class Shield(Weapon):
    def __init__(self, name, protection, durability, damage, penetration, ability):
        super(Shield, self).__init__(name)
        self.protection = protection
        self.durability = durability
        self.damage = damage
        self.ability = ability
        self.penetration = penetration


class Demonitizer(Weapon):
    def __init__(self, name, ammo, accuracy, damage, penetration, ability):
        super(Demonitizer, self).__init__(name)
        self.ammo = ammo
        self.range = accuracy
        self.damage = damage
        self.ability = ability
        self.penetration = penetration


class Throwable(Weapon):
    def __init__(self, name, ammo, damage, penetration, ability):
        super(Throwable, self).__init__(name)
        self.ammo = ammo
        self.damage = damage
        self.ability = ability
        self.penetration = penetration

    def throwable(self):
        print("You have %s %s" % (self.ammo, self.name))


class Clothing(Item):
    def __init__(self, name):
        super(Clothing, self).__init__(name)


class ChestPlate(Clothing):
    def __init__(self, name, protection, durability, flexibility):
        super(ChestPlate, self).__init__(name)
        self.protection = protection
        self.durability = durability
        self.flexibility = flexibility


class Shoes(Clothing):
    def __init__(self, name, speed, durability, jump, grip):
        super(Shoes, self).__init__(name)
        self.speed = speed
        self.durability = durability
        self.jump = jump
        self.grip = grip


class Leggings(Clothing):
    def __init__(self, name, protection, durability, space, flexibility):
        super(Leggings, self).__init__(name)
        self.protection = protection
        self.durability = durability
        self.space = space
        self.flexibility = flexibility


"""
class Helmet(Clothing):
    def __init__(self, name, fast_travel):
        super(Helmet, self).__init__(name)
"""

# Chest Plates
hackermans_chestplate = ChestPlate("Hacker Mans Chestplate", 0, -1, None)
gold_chestplate = ChestPlate("Golden ChestPlate", .80, 70, None)
chainmail_chestplate = ChestPlate("Chainmail ChestPlate", .80, 100, None)
kevlar_chestPlate = ChestPlate("Kevlar Chestplate", .60, 200, None)

# Melee Weapons
wood_sword = Sword("Wooden Sword", 50, 20, 0, None)
iron_sword = Sword("Sword", 100, 20, .10, None)
hackermans_sword = Sword("HM_Sword", -1, 42069, 1, None)
wood_board = Shield("Wood Board", .10, 50, 5, 0, None)
generations_sword = Sword("A Sword With A Long History", 99999999999999, 70, .40, None)


# Throwables
bazinga = Throwable("Bazinga", 1, 730, None, None)
dynamite = Throwable("Sticks of Dynamite", 3, 50, None, None)
can = Throwable('Can', 1, 2, None, None)
rock = Throwable('Rock', 1, 5, None, None)

# Demonitizers
AWP = Demonitizer("AWP", 10, 50, 115, None, None)
skraaa = Demonitizer("The Skraaa", 20, 90, 25, None, None)
lmb = Demonitizer("Light Machine Blaster", 45, 40, 40, None, None)
elon_musket = Demonitizer("A Elon Musket", 20, 10, 250, None, None)

# Potions
healthpotion1 = Potion("Level 1 Health Potion", 50, None, None, 1)
holywater = Potion("Holy Water", 500, None, None, 1)

# Food
bread = Food('Bread', 10, 10, None, None)
apple = Food('Apple', 5, 15, None, None)
pizza = Food('Pizza Pie', 40, 50, None, None)
sandwich = Food('Sandwich', 20, 25, None, None)
berries = Food('Berries', 2, 3, None, None)
chicken = Food('Chicken', 25, 35, None, None)


# Character
class Character(object):
    def __init__(self, name: str, health: int, weapon, clothes):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.clothes = clothes

    def take_damage(self, damage: int):
        if self.clothes is None:
            self.health -= damage
            if self.health <= 0:
                print("You killed it")
        else:
            self.health -= self.weapon.damage * self.clothes.protection
            if self.health <= 0:
                print("You killed it")
        print("%s had %d left" % (self.name, self.health))

    def attack(self, target):
        if self.clothes is None:
            print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
            target.take_damage(self.weapon.damage)
        else:
            print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
            target.take_damage(self.weapon.damage)


skeleton = Character("Skelly Boy", 120, iron_sword, gold_chestplate)
skeleton2 = Character("Spooky Boy", 120, wood_sword, gold_chestplate)
blubber_boy = Character("Blubber Boy", 250, wood_sword, None)
hacker = Character("Hacker", 9999, hackermans_sword, hackermans_chestplate)


# Room/Player
class Room(object):
    def __init__(self, name, east, north, south, west, northeast, description, items=None, npc=None):
        if npc is None:
            npc = []
        if items is None:
            items = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.northeast = northeast
        self.description = description
        self.items = items
        self.npc = npc


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.health = 150
        self.inventory = []

    def take(self):
        self.inventory.append(command.lower[5:])

    def find_next_room(self, direction):
        """This method searches the current room to use if a room exists in that direction

        :param direction: The direction that you want to move
        :return: The room object if it exists, or move if it can
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]

    def move(self, new_location):
        """

        :param new_location: The room object of which you are in
        """
        self.current_location = new_location


"""
#option 1 - Define as we go
R19A = Room("Mr Wiebe's Room")
parking_lot = Room("Parking Lot", None, R19A)

R19A, north = parking_lot

# Option 2 - Set all at once, modify controller
R19A = Room("Mr Wiebe's Room", 'parking_lot', None, None, None)
parking_lot = Room("Parking Lot", None, 'R19A', None, None)
"""
T_Spawn = Room("T Spawn", 'outside_long', 'top_mid', None, 'upper_b', None, "You are in T Spawn, East of you is "
                                                                            "outside of long, North is top of mid, "
                                                                            "West leads to upper b",
               [generations_sword])
outside_long = Room("Outside of Long", None, 'blue', 'T_Spawn', 'top_mid', None, "You are outside of long, North of you"
                                                                                 "is blue, South goes to T Spawn, and "
                                                                                 "West goes to the top of mid",
                    [])
blue = Room("Blue Bin", 'long', None, 'outside_long', None, None, "You're at blue, East of you is long, and South goes "
                                                                  "outside of long.",
            [])
long = Room("Long", None, 'ramp', 'blue', 'ct_ramp', None, "You're on a long path, North of you is ramp, South is blue,"
                                                           "and West is CT  ramp",
            [])
ramp = Room("Ramp", None, None, 'long', 'a_site', None, "You're on a ramp, South is long and West is A SITE",
            [AWP])
a_site = Room("A SITE", 'ramp', None, 'ct_ramp', 'a_plat', None, "You're on A SITE, East is ramp, you can drop South "
                                                                 "onto CT ramp, and west is A plat",
              [])
a_plat = Room("A Plat", 'a_site', None, 'cat', None, None, "You're on A plat, East is A SITE and South is cat",
              [])
cat = Room("Cat", 'a_plat', None, 'top_mid', 'mid', None, 'You are on cat, East is A plat, South is top mid,'
                                                          ' West is mid',
           [])
top_mid = Room("Top of Mid", 'outside_long', 'mid', None, None, 'cat', "You are top of mid, North is mid,"
                                                                       " Northeast is cat, East is outside of long ",
               [])
mid = Room("Mid", 'cat', 'ct_mid', 'top_mid', 'lower_b', None, "You are at mid, East is cat, North is CT mid, South is "
                                                               "top of mid, West is lower B",
           [])
ct_mid = Room("CT Mid", 'CT_Spawn', None, 'mid', 'outside_b', None, "You ar at CT mid, South is mid, East is CT Spawn, "
                                                                    "West is goes to outside of B",
              [], [])
CT_Spawn = Room("CT Spawn", 'ct_ramps', None, None, 'ct_mid', None, "You are in CT Spawn, West is CT mid,"
                                                                    " East is CT ramp",
                [], )
ct_ramp = Room("CT Ramp", 'CT_Spawn', None, None, 'long', None, "You are on CT ramp, West is CT Spawn, East is long.",
               [])
outside_b = Room("Outside of B Site", 'ct_mid', 'window', None, 'b_site', None, "You are outside of B, East is CT mid, "
                                                                                "West is B site, North is Window.",
                 [])
window = Room("Window", 'b_site', None, 'outside_b', 'ct_mid', None, "",
              [])
b_site = Room("B SITE", 'outside_b', None, 'upper_b', 'backplat', None, "",
              [])
backplat = Room("Back Plat", None, None, 'upper_b', 'b_site', None, "",
                [])
upper_b = Room("Upper B", 'lower_b', 'backplat', 'T_Spawn', None, None, "",
               [])
lower_b = Room("Lower B", 'mid', None, None, 'upper_b', None, "",
               [])

player = Player(T_Spawn)

playing = True
directions = ['north', 'south', 'east', 'west', 'northeast', 'up', 'down']
short_directions = ('n', 's', 'e', 'w', 'ne', 'u', 'd')
take = ['grab', 'take']
chckinv = ['inventory', 'items', 'check inventory']
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]
        print(command.lower())
    elif command.lower() in chckinv:
        print(player.inventory)
    elif command.lower() in take:
        try:
            if command.lower()[5:] == "take ":
                if len(player.current_location.items) > 0:
                    if player.current_location.items == command.lower()[:5]:
                        player.inventory.append(command.lower()[:5])
        except KeyError:
            print("You cannot take it")

    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command.lower())
            player.move(next_room)
        except KeyError:
            print("I can't go that way!")
    else:
            print("Command Not Found")



# Items
class Item(object):
    def __init__(self, name):
        self.name = name


# class Consumable(Item):
#     def __init__(self, name):
#         super(Consumable, self).__init__(name)
#
#
# class Potion(Consumable):
#     def __init__(self, name, heal, buff, debuff, amount):
#         super(Potion, self).__init__(name)
#         self.heal = heal
#         self.buff = buff
#         self.debuff = debuff
#         self.hunger = 0
#         self.amount = amount
#
#     def consume(self):
#         self.amount -= 1
#         print("You gained %s health" % self.heal)
#
#
# class Food(Consumable):
#     def __init__(self, name, hunger, heal, buff, debuff):
#         super(Food, self).__init__(name)
#         self.hunger = hunger
#         self.heal = heal
#         self.buff = buff
#         self.debuff = debuff


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
kevlar = ChestPlate("Golden ChestPlate", .80, 70, None)
chainmail_chestplate = ChestPlate("Chainmail ChestPlate", .80, 100, None)
kevlar_chestPlate = ChestPlate("Kevlar Chestplate", .60, 200, None)

# Melee Weapons
wood_sword = Sword("Sword", 50, 20, 0, None)
iron_sword = Sword("Sword", 100, 20, .10, None)
hackermans_sword = Sword("HM_Sword", -1, 42069, 1, None)
wood_board = Shield("Wood Board", .10, 50, 5, 0, None)
generations_sword = Sword("The Sword Of Many Generations", 9999999, 70, .40, None)


# Throwables
bazinga = Throwable("Bazinga", 1, 730, None, None)
dynamite = Throwable("Sticks of Dynamite", 3, 50, None, None)

# Demonitizers
dragonlore = Demonitizer("DragonLore", 10, 50, 115, None, None)
skraaa = Demonitizer("The Skraaa", 20, 90, 25, None, None)
lmb = Demonitizer("Light Machine Blaster", 45, 40, 40, None, None)
elon_musket = Demonitizer("A Elon Musket", 20, 10, 250, None, None)

# # Potions
# HealthPotion1 = Potion("Level 1 Health Potion", 50, None, None, 1)
#
# # Food
# bread = Food('Bread', 10, 10, None, None)
# apple = Food('Apple', 5, 15, None, None)
# pizza = Food('Pizza Pie', 40, 50, None, None)
# sandwich = Food('Sandwich', 20, 25, None, None)
# berries = Food('Berries', 2, 3, None, None)


# Character
class Character(object):
    def __init__(self, name: str, health: int, weapon, clothes):
        self.name = name
        self.health = health
        self.damage = weapon
        self.clothes = clothes

    def take_damage(self, damage: int):
        if self.clothes is None:
            self.health -= damage
            if self.health <= 0:
                print("You killed it")
        else:
            self.health -= self.damage.damage * self.clothes.protection
            if self.health <= 0:
                print("You killed it")
        print("%s had %d left" % (self.name, self.health))

    def attack(self, target):
        if self.clothes is None:
            print("%s attacks %s for %d damage" % (self.name, target.name, self.damage))
            target.take_damage(self.damage)
        else:
            print("%s attacks %s for %d damage" % (self.name, target.name, self.damage))
            target.take_damage(self.damage)


bad_guy_defender = Character("Bad Guy Defender", 100, 20, kevlar)
bad_guy_attacker = Character("Bad Guy Attacker", 100, 20, kevlar)
flanker = Character("Flanker", 200, 25, kevlar)
hacker = Character("Hacker", 450, 42069, None)
awper = Character("Awper", 100, 450, None)


# Room/Player
class Room(object):
    def __init__(self, name, east, north, south, west, northeast, description, npc, items=None):
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
        self.maxhealth = 150
        self.health = 100
        self.weapon = []
        self.heal = 5

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
                                                                            "West leads to upper b.\n This is where the"
                                                                            " "
                                                                            "T team spawns and also where an awper can"
                                                                            "try to stop someone passing through mid",
               [], None)
outside_long = Room("Outside of Long", None, 'blue', 'T_Spawn', 'top_mid', None, "You are outside of long. "
                                                                                 " \n North of you"
                                                                                 "is blue, South goes to T Spawn, and "
                                                                                 "West goes to the top of mid",
                    [], bad_guy_attacker)
blue = Room("Blue Bin", 'long', None, 'outside_long', None, None, "You're at blue, East of you is long, and South goes "
                                                                  "outside of long.",
            [], None)
long = Room("Long", None, 'ramp', 'blue', 'ct_ramp', None, "You're on a long path, North of you is ramp, South is blue,"
                                                           "and West is CT  ramp.\n Long range weapons are most "
                                                           "effective here",
            [], None)
ramp = Room("Ramp", None, None, 'long', 'a_site', None, "You're on a ramp, South is long and West is A SITE",
            [], None)
a_site = Room("A SITE", 'ramp', None, 'ct_ramp', 'a_plat', None, "You're on A SITE, East is ramp, you can drop South "
                                                                 "onto CT ramp, and west is A plat.\nWatch out for "
                                                                 "awpers in this location, CT must defend this"
                                                                 " site while the T must take it",
              [], hacker)
a_plat = Room("A Plat", 'a_site', None, 'cat', None, None, "You're on A plat, East is A SITE and South is cat",
              [], None)
cat = Room("Cat", 'a_plat', None, 'top_mid', 'mid', None, 'You are on cat, East is A plat, South is top mid,'
                                                          ' West is mid.\nWatch out for CT flankers where they will '
                                                          'watch lower or try to flank into long ',
           [], flanker)
top_mid = Room("Top of Mid", 'outside_long', 'mid', None, None, 'cat', "You are top of mid, North is mid,"
                                                                       " Northeast is cat, East is outside of long\n"
                                                                       "You are a clear shot for an awper up here ",
               [], None)
mid = Room("Mid", 'cat', 'ct_mid', 'top_mid', 'lower_b', None, "You are at mid, East is cat, North is CT mid, South is "
                                                               "top of mid, West is lower B."
                                                               "\nWatch out for awpers down"
                                                               " in CT mid",
           [], None)
ct_mid = Room("CT Mid", 'CT_Spawn', None, 'mid', 'outside_b', None, "You are at CT mid. West is outside of B, South is"
                                                                    "Mid, and East is CT Spawn.\nThis is where an "
                                                                    "awper an awper would be",
              [], awper)
CT_Spawn = Room("CT Spawn", 'ct_ramps', None, None, 'ct_mid', None, "You are in CT Spawn. West is Ct mid, East is CT "
                                                                    "ramp.\nThis is the CT team spawns",
                [], None)
ct_ramp = Room("CT Ramp", 'CT_Spawn', None, None, 'long', None, "This is CT ramp, East is Long, West is CT Spawn",
               [], None)
outside_b = Room("Outside of B Site", 'ct_mid', 'window', None, 'b_site', None, "This is outside of B, North is window,"
                                                                                "East is B site, West is CT mid",
                 [], None)
window = Room("Window", 'b_site', None, 'outside_b', 'ct_mid', None, "This is B site's window, West is CT mid, East is"
                                                                     " B site, South is outside of B.\n"
                                                                     "an awper would be here watching people either"
                                                                     "entering CT mid or exiting upper B",
              [], None)
b_site = Room("B SITE", 'outside_b', None, 'upper_b', 'backplat', None, "You are on B site, West is outside of B, "
                                                                        "South is upper B, East is backplat.\n"
                                                                        "CT must defend this site while the T must take"
                                                                        " it",
              [], None)
backplat = Room("Back Plat", None, None, 'upper_b', 'b_site', None, "This is back plat, South is upper B, and West is "
                                                                    "B site.\nWatch out people holding long angles "
                                                                    "here",
                [], bad_guy_defender)
upper_b = Room("Upper B", 'lower_b', 'backplat', 'T_Spawn', None, None, "This is upper B, West is lower B, North is"
                                                                        "Backplat, South is T Spawn.\nThere is a long"
                                                                        " narrow tunnel to B site where you can easily"
                                                                        " get hurt",
               [], None)
lower_b = Room("Lower B", 'upper_b', None, None, 'mid', None, "Lower B is where you are, West is mid, East is upper B",
               [], None)
picking = True
playing = False
while picking:
    answer = input("Where you like to spawn? (T/CT)\n> ")
    if answer.lower().strip() == 't':
        player = Player(T_Spawn)
        playing = True
        picking = False
    if answer.lower().strip() == 'ct':
        player = Player(CT_Spawn)
        playing = True
        picking = False
    else:
        continue

directions = ['north', 'south', 'east', 'west', 'northeast', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'ne', 'u', 'd']
take = ['grab', 'take']
stats = ['check health', 'health', 'stats']
heal = ['heal']
chckinv = ['inventory', 'items', 'check inventory']
enemy_rooms = ['Outside of Long','Back Plat', 'CT Mid', 'A SITE', 'Cat']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input("> ")
    if player.current_location.name in enemy_rooms:
        print("There is an enemy here! It's %s" % Room.npc)
    if player.health > player.maxhealth:
        player.health = player.maxhealth
    if player.health <= 0:
        print("You Died! \nTry Again!")
        playing = False
    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]
        print(command.lower())
    if command.lower() in heal:
        if player.health < player.maxhealth:
            player.health += 50
            print("You healed yourself! \nYour health is: %s " % player.health)
            player.heal -= 1
        else:
            print("You can't or do not need to heal.")
            continue
    if command.lower() in stats:
        print('''
        ----------------------------------------------------------------------------------------------------------------
        Health: %s
        Weapon: %s
        Healing Items Left: %s
        Current Location: %s
        ----------------------------------------------------------------------------------------------------------------
        
        ''' % (player.health, player.weapon, player.heal, player.current_location.name))
    if command.lower() in directions:
        try:
            next_room = player.find_next_room(command.lower())
            player.move(next_room)
        except KeyError:
            print("I can't go that way!")
    # elif command.lower()[0:6] == "attack":
    # if command.lower() in chckinv:
    #     print(player.inventory)


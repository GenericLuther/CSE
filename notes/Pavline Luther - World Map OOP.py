class Room(object):
    def __init__(self, name, east, north, south, west, northeast, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.northeast = northeast
        self.description = description


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
                                                                            "outside of long, North is top of mid"
                                                                            "West leads to upper b")
outside_long = Room("Outside of Long", None, 'blue', 'T_Spawn', 'top_mid', None, "You are outside of long, North of you"
                                                                                 "is blue, South goes to T Spawn, and "
                                                                                 "West goes to the top of mid")
blue = Room("Blue Bin",'long', None, 'outside_long', None, None, "You're at blue, East of you is long, and South goes "
                                                                 "outside of long.")
long = Room("Long", None, 'ramp', 'blue', 'ct_ramp', None, "You're on a long path, North of you is ramp, South is blue,"
                                                           "and West is CT  ramp")
ramp = Room("Ramp", None, None, 'long', 'a_site', None, "You're on a ramp, South is long and West is A SITE")
a_site = Room("A SITE", 'ramp', None, 'ct_ramp', 'a_plat', None, "You're on A SITE, East is ramp, you can drop South "
                                                                 "onto CT ramp, and west is A plat")
a_plat = Room("A Plat", 'a_site', None, 'cat', None, None, "")
cat = Room("Cat", 'a_plat', None, 'top_mid','mid', None)
top_mid = Room("Top of Mid", 'outside_long', 'mid', None, None, 'cat')
mid = Room("Mid", 'cat', 'ct_mid', 'top_mid', 'lower_b', None)
ct_mid = Room("CT Mid", 'CT_Spawn', None, 'mid', 'outside_b', None)
CT_Spawn = Room("CT Spawn", 'ct_ramps', None, None, 'ct_mid', None)
ct_ramp = Room("CT Ramp", 'CT_Spawn', None, None, 'long', None)
outside_b = Room("Outside of B Site", 'ct_mid', 'window', None, 'b_site', None)
window = Room("Window", 'b_site', None, 'outside_b', 'ct_mid', None)
b_site = Room("B SITE", 'outside_b', None, 'upper_b', 'backplat', None)
backplat = Room("Back Plat", None, None, 'upper_b', 'b_site', None)
upper_b = Room("Upper B", 'lower_b', 'backplat', 'T_Spawn', None, None)
lower_b = Room("Lower B", 'mid', None, None, 'upper_b', None)

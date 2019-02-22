class Room(object):
    def __init__(self, name, east, north, south, west, northeast):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.northeast = northeast


"""
#option 1 - Define as we go
R19A = Room("Mr Wiebe's Room")
parking_lot = Room("Parking Lot", None, R19A)

R19A, north = parking_lot

# Option 2 - Set all at once, modify controller
R19A = Room("Mr Wiebe's Room", 'parking_lot', None, None, None)
parking_lot = Room("Parking Lot", None, 'R19A', None, None)
"""
T_Spawn = Room("T Spawn", 'outside_long', 'suicide', None, 'upper_b', None)
outside_long = Room("Outside of Long", None, 'blue', 'T_Spawn', 'top_mid', None)
blue = Room("Blue Bin",'long', None, 'outside_long', None, None)
long = Room("Long", None, 'ramp', 'blue', 'ct_ramp', None)
ramp = Room("Ramp", None, None, 'long', 'a_site', None)
a_site = Room("A SITE", 'ramp', None, 'ct_ramp', 'a_plat', None)
a_plat = Room("A Plat", 'a_site', None, 'cat', None, None)
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
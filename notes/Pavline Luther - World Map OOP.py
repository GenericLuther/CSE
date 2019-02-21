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
T_Spawn = Room("T Spawn", 'outside_long', 'suicide',None, 'upper_b')
outside_long = Room("Outside of Long",None, 'blue', 'T_Spawn', 'top_mid')
blue = Room("Blue Bin",'long',None, 'outside_long', None)
long = Room("Long",None, 'ramp', 'blue', 'ct_ramp')
ramp = Room("Ramp", None, None, 'long', 'a_site')
a_site = Room("A SITE", 'ramp', None, 'ct_ramp', 'a_plat')
a_plat = Room("A Plat", 'a_site', None, 'cat', None)
cat = Room("Cat", 'a_plat', None, 'top_mid','mid')
top_mid = Room("Top of Mid", )

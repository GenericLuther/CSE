class Room(object):
    def __init__(self, name, east, north=False,south=False):
        self.name = name
        self.north = north
        self.south = south
        self.east = east


#option 1 - Define as we go
R19A = Room("Mr Wiebe's Room")
parking_lot = Room("Parking Lot", None, R19A)

R19A, north = parking_lot

# Option 2 - Set all at once, modify controller
R19A = Room("Mr Wiebe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, 'R19A')
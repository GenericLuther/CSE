world_map_example = {
    "R19A": {
        "NAME": "Mr.Wiebe's Room",
        "DESCRIPTION": "This is the classroom you are in right "
                       "now. There are two doors on the north wall.",
        "PATHS": {
            "NORTH": "PARKING_LOT"
            }
        },
    "PARKING_LOT": {
        "NAME": " The North Parking Lot",
        "DESCRIPTION": "There are a couple cars parked here.",
        "PATHS": {
            "SOUTH": 'R19A'
            }
        }
    }
"""
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "EAST": '',
            "WEST": '',
            "NORTH": '',
            "SOUTH": ''
            }
"""

de_dust2 = {
    "T_SPAWN": {
        "NAME": "T Spawn ",
        "DESCRIPTION": "You are in the T sides spawn."
                       "East is a ramp that leads to two more paths"
                       "West leads to upper B"
                       "North goes through a small alley way, going here would be suicide if they are prepared ",
        "PATHS": {
            "EAST": 'OUTSIDE_LONG',
            "WEST": 'UPPER_B',
            "NORTH": 'SUICIDE'
            }
    },
    "OUTSIDE_LONG": {
        "NAME": "Outside of Long",
        "DESCRIPTION": "You are outside of long, there are three paths"
                       "North of you is the entrance to long"
                       "West of you is mid"
                       "South is T spawn",
        "PATHS": {
            "WEST": 'TOP_OF_MID',
            "NORTH": 'BLUE',
            "SOUTH": 'T_SPAWN'
        }
    },
    "BLUE": {
        "NAME": "Blue",
        "DESCRIPTION": "You are at blue bin."
                       "do you want to go north up long,"
                       "or do you want to go east into pit?",
        "PATHS": {
            "EAST": 'PIT',
            "NORTH": 'LONG',
            "SOUTH": 'OUTSIDE_LONG'
        }
    },
    "PIT": {
        "NAME": "Pit",
        "DESCRIPTION": "You are in cover but there is only one way to go and that is north.",
        "PATHS": {
            "NORTH": 'LONG'
        }
    },
    "LONG": {
        "NAME": "Long",
        "DESCRIPTION": "This a long path up north to A site by going up ramp."
                       "East of you is car for cover"
                       "West of you is CT ramp"
                       "South of you goes to blue bin",
        "PATHS": {
            "EAST": 'CAR',
            "WEST": 'CT_RAMP',
            "NORTH": 'RAMP',
            "SOUTH": 'BLUE'
        }
    },
    "CAR": {
        "NAME": "Car",
        "DESCRIPTION": "You are behind cover which happens to be a car."
                       "North of you is ramp"
                       "South of you is long"
                       "West of you is CT ramp",
        "PATHS": {
            "WEST": 'CT_RAMP',
            "NORTH": 'RAMP',
            "SOUTH": 'LONG'
            }
    },
    "RAMP": {
        "NAME": "Ramp",
        "DESCRIPTION": "You are on a ramp right by A site"
                       "North of you is Goose"
                       "South is long"
                       "West is A site",
        "PATHS": {
            "WEST": 'A_SITE',
            "NORTH": 'GOOSE',
            "SOUTH": 'LONG'
        }
    },
    "GOOSE": {
        "NAME": "Goose",
        "DESCRIPTION": "You are at Goose, you got cover from cat"
                       "South of you is A site",
        "PATHS": {
            "SOUTH": 'A_SITE'
        }
    },
    "A_SITE": {
        "NAME": "A Site",
        "DESCRIPTION": "You have taken control of A site"
                       "East of you is ramp"
                       "West of you is A plat"
                       "South you can jump off to get CT ramp"
                       "North of you is Goose",
        "PATHS": {
            "EAST": 'RAMP',
            "WEST": 'A_PLAT',
            "NORTH": 'GOOSE',
            "SOUTH": 'CT_RAMP'
        }
    },
    "A_PLAT": {
        "NAME": "A Plat",
        "DESCRIPTION": "You are on A plat, you are in a open area."
                       "South of you is short"
                       "East of you is A site",
        "PATHS": {
            "EAST": 'A_SITE',
            "SOUTH": 'SHORT'
        }
    },
    "SHORT": {
        "NAME": "Short",
        "DESCRIPTION": "You are on short A"
                       "South of you is cat that leads to catwalk"
                       "If you jump towards East you will land on CT ramp"
                       "North of you is A plat",
        "PATHS": {
            "EAST": 'CT_RAMP',
            "NORTH": 'A_PLAT',
            "SOUTH": 'CATWALK'
        }
    },
    "CATWALK": {
        "NAME": "Catwalk",
        "DESCRIPTION": "You are on catwalk"
                       "West of you is mid"
                       "East of you is cat to short"
                       "South goes to top of mid",
        "PATHS": {
            "EAST": 'SHORT',
            "WEST": 'MID',
            "SOUTH": 'TOP_MID'
        }
    },
    "TOP_MID": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "EAST": '',
            "WEST": '',
            "NORTH": '',
            "SOUTH": ''
        }
    }

}
# Controller
playing = True
current_node = world_map_example['R19A']
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False

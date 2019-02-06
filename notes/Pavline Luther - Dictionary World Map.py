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
        "DESCRIPTION": "East is a ramp that leads to two more paths."
                       "West leads to upper B."
                       "North goes through a small alley way, going here would be suicide if they are prepared. ",
        "PATHS": {
            "EAST": 'OUTSIDE_LONG',
            "WEST": 'UPPER_B',
            "NORTH": 'SUICIDE'
            }
    },
    "OUTSIDE_LONG": {
        "NAME": "Outside of Long",
        "DESCRIPTION": "North of you is the entrance to long"
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
        "DESCRIPTION": "You are at blue bin"
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
        "DESCRIPTION": "You are in cover but there is only one way to go and that is north",
        "PATHS": {
            "NORTH": 'LONG'
        }
    },
    "LONG": {
        "NAME": "Long",
        "DESCRIPTION": "This a long path up north to A site by going up ramp."
                       "East of you is car for cover."
                       "West of you is CT Ramp"
                       "South of you goes to blue bin",
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

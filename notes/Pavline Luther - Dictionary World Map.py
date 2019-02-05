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
de_dust2 = {
    "T_SPAWN": {
        "NAME": "T Spawn ",
        "DESCRIPTION": "East is a ramp that leads to two more paths."
                       "West leads to upper B"
                       "North goes through a small alley way, going here would be suicide if they are prepared ",
        "PATHS": {
            "EAST": 'OUTSIDE_LONG',
            "WEST": 'UPPER_B',
            "NORTH": 'SUICIDE'
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

states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"
}

print(states["CA"])
print(states["AK"])

neated_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000
    }
}

print(neated_dictionary["GA"]["POPULATION"])
print(neated_dictionary["FL"]["NAME"])

print(neated_dictionary["GA"])

georgia = neated_dictionary["GA"]
print(georgia)

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": {
            "Fresno",
            "San Francisco",
            "Los Angeles"
        }
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000,
        "CITIES": {
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville"
        }
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,
        "CITIES": {
            "Anchorage",
            "Fairbanks",
            "Juneau"
        }
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000,
        "CITIES": {
            "Atlanta",
            "Savannah",
            "Augusta"
        }
    }
}

print(complex_dictionary["AK"]["CITIES"][0])

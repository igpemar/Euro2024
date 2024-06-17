# import main

bracketMap_24 = {
    "ABCD": {
        "1B": "3A",  ## this is our match
        "1C": "3D",
        "1E": "3B",
        "1F": "3C",
        "1A": "2C",
        "1D": "2F",
        "2A": "2B",
        "2D": "2E",
    },
    "ABCE": {
        "1B": "3A",
        "1C": "3E",
        "1E": "3B",
        "1F": "3C",
        "1A": "2C",
        "1D": "2F",
        "2A": "2B",
        "2D": "2E",
    },
    "ABCF": {
        "1B": "3A",
        "1C": "3F",
        "1E": "3B",
        "1F": "3C",
        "1A": "2C",
        "1D": "2F",
        "2A": "2B",
        "2D": "2E",
    },
    "ABDE": {
        "1B": "3D",
        "1C": "3E",
        "1E": "3A",
        "1F": "3B",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "ABDF": {
        "1B": "3D",
        "1C": "3F",
        "1E": "3A",
        "1F": "3B",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "ABEF": {
        "1B": "3E",
        "1C": "3F",
        "1E": "3B",
        "1F": "3A",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "ACDE": {
        "1B": "3E",
        "1C": "3D",
        "1E": "3C",
        "1F": "3A",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "ACDF": {
        "1B": "3F",
        "1C": "3D",
        "1E": "3C",
        "1F": "3A",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "ACEF": {
        "1B": "3E",
        "1C": "3F",
        "1E": "3C",
        "1F": "3A",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "ADEF": {
        "1B": "3E",
        "1C": "3F",
        "1E": "3D",
        "1F": "3A",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "BCDE": {
        "1B": "3E",
        "1C": "3D",
        "1E": "3B",
        "1F": "3C",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "BCDF": {
        "1B": "3F",
        "1C": "3D",
        "1E": "3C",
        "1F": "3B",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "BCEF": {
        "1B": "3F",
        "1C": "3E",
        "1E": "3C",
        "1F": "3B",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "BDEF": {
        "1B": "3F",
        "1C": "3E",
        "1E": "3D",
        "1F": "3B",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
    "CDEF": {
        "1B": "3F",
        "1C": "3E",
        "1E": "3D",
        "1F": "3C",
        "1D": "2F",
        "1A": "2C",
        "2A": "2B",
        "2D": "2E",
    },
}

bracketMap_8 = {"1B": "2A", "1A": "2B"}
bracketMap_16 = {"1B": "2A", "1A": "2B", "1C": "2D", "1D": "2C"}


def check_duplicate_values(bracketMap):
    for _, inner_dict in bracketMap.items():
        for value in inner_dict.values():
            values = set()
            if value in values:
                return True
            values.add(value)
    return False


def get_bracket_map(q_tag: str) -> dict:
    if q_tag == "":
        return bracketMap_16
    for key, bracket in bracketMap_24.items():
        for c in q_tag:
            if c not in key:
                break
        else:
            return bracket
    else:
        raise Exception(f"Bracket not found for {q_tag}")


if check_duplicate_values(bracketMap_24):
    raise Exception("Duplicate values found in bracketMap")
else:
    print("No duplicate values found in bracketMap")

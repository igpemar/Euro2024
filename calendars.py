calendarA = [
    ["Germany", "Scotland", 5, 1, True],
    ["Hungary", "Switzerland", 1, 3, True],
    ["Germany", "Hungary", 2, 0, True],
    ["Scotland", "Switzerland", 1, 1, True],
    ["Switzerland", "Germany", 1, 1, True],
    ["Scotland", "Hungary", 0, 1, True],
]
calendarB = [
    ["Spain", "Croatia", 3, 0, True],
    ["Italy", "Albania", 2, 1, True],
    ["Croatia", "Albania", 2, 2, True],
    ["Spain", "Italy", 1, 0, True],
    ["Albania", "Spain", 0, 1, True],
    ["Croatia", "Italy", 1, 1, True],
]
calendarC = [
    ["Slovenia", "Denmark", 1, 1, True],
    ["Serbia", "England", 0, 1, True],
    ["Slovenia", "Serbia", 1, 1, True],
    ["Denmark", "England", 2, 2, True],
    ["Denmark", "Serbia", 0, 0, True],
    ["England", "Slovenia", 0, 0, True],
]
calendarD = [
    ["Poland", "Netherlands", 1, 2, True],
    ["Austria", "France", 0, 1, True],
    ["Poland", "Austria", 1, 3, True],
    ["Netherlands", "France", 0, 0, True],
    ["Netherlands", "Austria", 2, 3, True],
    ["France", "Poland", 1, 1, True],
]
calendarE = [
    ["Romania", "Ukraine", 3, 0, True],
    ["Belgium", "Slovakia", 0, 1, True],
    ["Slovakia", "Ukraine", 1, 2, True],
    ["Belgium", "Romania", 2, 0, True],
    ["Ukraine", "Belgium", -1, -1, True],
    ["Slovakia", "Romania", -1, -1, True],
]
calendarF = [
    ["Turkey", "Georgia", 3, 1, True],
    ["Portugal", "Czechia", 2, 1, True],
    ["Georgia", "Czechia", 1, 1, True],
    ["Turkey", "Portugal", 0, 3, True],
    ["Czechia", "Turkey", -1, -1, True],
    ["Georgia", "Portugal", -1, -1, True],
]


def count_all_occurrences(calendarA):
    # Flatten the list of lists
    from collections import Counter

    flattened_list = [
        item for sublist in calendarA for item in sublist if isinstance(item, str)
    ]
    # Use Counter to count occurrences of each string
    return Counter(flattened_list)


if len(calendarA) != 6:
    raise Exception("calendarA is missing matches")
elif len(calendarB) != 6:
    raise Exception("calendarB is missing matches")
elif len(calendarC) != 6:
    raise Exception("calendarC is missing matches")
elif len(calendarD) != 6:
    raise Exception("calendarD is missing matches")
elif len(calendarE) != 6:
    raise Exception("calendarE is missing matches")
elif len(calendarF) != 6:
    raise Exception("calendarF is missing matches")
else:
    print("All calendars have the righ number of matches")

occurrences = count_all_occurrences(calendarA)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
occurrences = count_all_occurrences(calendarB)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
occurrences = count_all_occurrences(calendarC)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
occurrences = count_all_occurrences(calendarD)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
occurrences = count_all_occurrences(calendarE)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
occurrences = count_all_occurrences(calendarF)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
print("All teams within each calendars play exactly 3 matches")

G = 0
for match in calendarA:
    if match[2] != -1 and match[4]:
        G += 1
for match in calendarB:
    if match[2] != -1 and match[4]:
        G += 1
for match in calendarC:
    if match[2] != -1 and match[4]:
        G += 1
for match in calendarD:
    if match[2] != -1 and match[4]:
        G += 1
for match in calendarE:
    if match[2] != -1 and match[4]:
        G += 1
for match in calendarF:
    if match[2] != -1 and match[4]:
        G += 1

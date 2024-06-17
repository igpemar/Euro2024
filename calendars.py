calendarA = [
    # ["Germany", "Scotland", 5, 1],
    # ["Hungary", "Switzerland", 1, 3],
    ["Germany", "Scotland", -1, -1],
    ["Hungary", "Switzerland", -1, -1],
    ["Germany", "Hungary", -1, -1],
    ["Scotland", "Switzerland", -1, -1],
    ["Switzerland", "Germany", -1, -1],
    ["Scotland", "Hungary", -1, -1],
]
calendarB = [
    # ["Spain", "Croatia", 3, 0],
    # ["Italy", "Albania", 2, 1],
    ["Spain", "Croatia", -1, -1],
    ["Italy", "Albania", -1, -1],
    ["Croatia", "Albania", -1, -1],
    ["Spain", "Italy", -1, -1],
    ["Albania", "Spain", -1, -1],
    ["Croatia", "Italy", -1, -1],
]
calendarC = [
    # ["Slovenia", "Denmark", 1, 1],
    ["Slovenia", "Denmark", -1, -1],
    # ["Serbia", "England", 0, 1],
    ["Serbia", "England", -1, -1],
    ["Slovenia", "Serbia", -1, -1],
    ["Denmark", "England", -1, -1],
    ["Denmark", "Serbia", -1, -1],
    ["England", "Slovenia", -1, -1],
]
calendarD = [
    # ["Poland", "Netherlands", 1, 2],
    ["Poland", "Netherlands", -1, -1],
    ["Austria", "France", -1, -1],
    ["Poland", "Austria", -1, -1],
    ["Netherlands", "France", -1, -1],
    ["Netherlands", "Austria", -1, -1],
    ["France", "Poland", -1, -1],
]
calendarE = [
    ["Romania", "Ukraine", -1, -1],
    ["Belgium", "Slovakia", -1, -1],
    ["Slovakia", "Ukraine", -1, -1],
    ["Belgium", "Romania", -1, -1],
    ["Ukraine", "Belgium", -1, -1],
    ["Slovakia", "Romania", -1, -1],
]
calendarF = [
    ["Turkey", "Georgia", -1, -1],
    ["Portugal", "Czechia", -1, -1],
    ["Georgia", "Czechia", -1, -1],
    ["Turkey", "Portugal", -1, -1],
    ["Czechia", "Turkey", -1, -1],
    ["Georgia", "Portugal", -1, -1],
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
    if match[2] != -1:
        G += 1
for match in calendarB:
    if match[2] != -1:
        G += 1
for match in calendarC:
    if match[2] != -1:
        G += 1
for match in calendarD:
    if match[2] != -1:
        G += 1
for match in calendarE:
    if match[2] != -1:
        G += 1
for match in calendarF:
    if match[2] != -1:
        G += 1

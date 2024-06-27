calendar_A = [
    ["Germany", "Scotland", 5, 1],
    ["Hungary", "Switzerland", 1, 3],
    ["Germany", "Hungary", 2, 0],
    ["Scotland", "Switzerland", 1, 1],
    ["Switzerland", "Germany", 1, 1],
    ["Scotland", "Hungary", 0, 1],
]
calendar_B = [
    ["Spain", "Croatia", 3, 0],
    ["Italy", "Albania", 2, 1],
    ["Croatia", "Albania", 2, 2],
    ["Spain", "Italy", 1, 0],
    ["Albania", "Spain", 0, 1],
    ["Croatia", "Italy", 1, 1],
]
calendar_C = [
    ["Slovenia", "Denmark", 1, 1],
    ["Serbia", "England", 0, 1],
    ["Slovenia", "Serbia", 1, 1],
    ["Denmark", "England", 2, 2],
    ["Denmark", "Serbia", 0, 0],
    ["England", "Slovenia", 0, 0],
]
calendar_D = [
    ["Poland", "Netherlands", 1, 2],
    ["Austria", "France", 0, 1],
    ["Poland", "Austria", 1, 3],
    ["Netherlands", "France", 0, 0],
    ["Netherlands", "Austria", 2, 3],
    ["France", "Poland", 1, 1],
]
calendar_E = [
    ["Romania", "Ukraine", 3, 0],
    ["Belgium", "Slovakia", 0, 1],
    ["Slovakia", "Ukraine", 1, 2],
    ["Belgium", "Romania", 2, 0],
    ["Ukraine", "Belgium", 0, 0],
    ["Slovakia", "Romania", 1, 1],
]
calendar_F = [
    ["Turkey", "Georgia", 3, 1],
    ["Portugal", "Czechia", 2, 1],
    ["Georgia", "Czechia", 1, 1],
    ["Turkey", "Portugal", 0, 3],
    ["Czechia", "Turkey", 0, 1],
    ["Georgia", "Portugal", 2, 0],
]


def count_all_occurrences(calendar_A):
    # Flatten the list of lists
    from collections import Counter

    flattened_list = [
        item for sublist in calendar_A for item in sublist if isinstance(item, str)
    ]
    # Use Counter to count occurrences of each string
    return Counter(flattened_list)


if len(calendar_A) != 6:
    raise Exception("calendar_A is missing matches")
elif len(calendar_B) != 6:
    raise Exception("calendar_B is missing matches")
elif len(calendar_C) != 6:
    raise Exception("calendar_C is missing matches")
elif len(calendar_D) != 6:
    raise Exception("calendar_D is missing matches")
elif len(calendar_E) != 6:
    raise Exception("calendar_E is missing matches")
elif len(calendar_F) != 6:
    raise Exception("calendar_F is missing matches")

occurrences = count_all_occurrences(calendar_A)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
occurrences = count_all_occurrences(calendar_B)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
occurrences = count_all_occurrences(calendar_C)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
occurrences = count_all_occurrences(calendar_D)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
occurrences = count_all_occurrences(calendar_E)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
occurrences = count_all_occurrences(calendar_F)
for k, v in occurrences.items():
    if v != 3:
        raise Exception(f"Team {k} is missing matches")
print("All teams within each calendar_s play exactly 3 matches")

G = 0
for match in calendar_A:
    if match[2] >= 0:
        G += 1
for match in calendar_B:
    if match[2] >= 0:
        G += 1
for match in calendar_C:
    if match[2] >= 0:
        G += 1
for match in calendar_D:
    if match[2] >= 0:
        G += 1
for match in calendar_E:
    if match[2] >= 0:
        G += 1
for match in calendar_F:
    if match[2] >= 0:
        G += 1

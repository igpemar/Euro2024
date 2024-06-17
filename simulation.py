import random

fifa_ranking = {
    "France": 1,
    "Belgium": 2,
    "England": 3,
    "Portugal": 4,
    "Netherlands": 5,
    "Spain": 6,
    "Italy": 7,
    "Croatia": 8,
    "Germany": 9,
    "Switzerland": 10,
    "Denmark": 11,
    "Ukraine": 12,
    "Austria": 13,
    "Hungary": 14,
    "Poland": 15,
    "Serbia": 16,
    "Czechia": 17,
    "Scotland": 18,
    "Turkey": 19,
    "Romania": 20,
    "Slovakia": 21,
    "Slovenia": 22,
    "Albania": 23,
    "Georgia": 24,
}

MAX_RANDOM = 4
RANKING_BIASED_MAX_GAIN = 2


def random_sim(match):
    return (random.randint(0, MAX_RANDOM), random.randint(0, MAX_RANDOM))


def ranking_biased(match):
    import math

    home_team, away_team = match[0], match[1]
    gain = (
        RANKING_BIASED_MAX_GAIN
        * (fifa_ranking[home_team] - fifa_ranking[away_team])
        / 24
    )
    return math.floor(random.randint(0, MAX_RANDOM) - gain), math.floor(
        random.randint(0, MAX_RANDOM) + gain
    )

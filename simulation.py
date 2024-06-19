import bracket, simulation, group, counter
import pickle
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

ALLOW_THIRDS = True
MAX_RANDOM = 4
RANKING_BIASED_MAX_GAIN = 2
selected_country = "Spain"
select_match = "1B"


def random_sim(match):
    if match[0] == "Albania":
        return 5, 0
    if match[1] == "Albania":
        return 0, 5

    draw = random.random()
    if draw < 0.30:
        goals = random.randint(0, MAX_RANDOM)
        return goals, goals

    goals_h = random.randint(0, MAX_RANDOM)
    goals_a = random.randint(0, MAX_RANDOM)
    while goals_h == goals_a:
        goals_h = random.randint(0, MAX_RANDOM)
        goals_a = random.randint(0, MAX_RANDOM)
    return goals_h, goals_a


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


simulation_function = simulation.random_sim


def worker(N, index):
    qualified_directly, qualified_potentially, qualified_all = {}, {}, {}
    counter_all = counter.Counter("all_games")
    counter_country = counter.Counter(selected_country)
    counter_match = counter.Counter(select_match)
    for i in range(int(N)):
        bracket_string = ""
        print(
            f"P {index:02d}: Begin of simulation {i + 1}/{N}, {round((i+1)/N*100,3)}%"
        )
        ## Setup
        groups = group.initialize()

        ## Simulate pending matches
        for g in groups:
            # g.simulate(simulation.random_result)
            g.simulate(simulation_function)

        ## Update standings
        for g in groups:
            g.update_standings()

        ## Get direct qualified teams
        for g in groups:
            qualified_directly.update(g.qualifies())
        qualified_all.update(qualified_directly)

        # Get teams qualified as thirds
        for g in groups:
            qualified_potentially.update(g.qualifies([3]))
        if ALLOW_THIRDS:
            group_3rd = group.Group("3rd", [])
            group_3rd.teams = {i.name: i for i in qualified_potentially.values()}
            group_3rd.update_standings_3rd_group()
            qualified_3rd_group = group_3rd.qualifies([1, 2, 3, 4], override_tag=True)
            qualified_all.update(qualified_3rd_group)
            for key in qualified_3rd_group.keys():
                bracket_string += key[1]

        if (
            qualified_all["1B"].name
            == "Albania"
            # and qualified_all["3D"].name == "Austria"
        ):
            pass
        # Generate bracket
        selected_bracket = bracket.get(bracket_string)
        bracket_matches = bracket.get_matches(selected_bracket, qualified_all)

        # Count all matches
        for match in bracket_matches:
            counter_all.add(match)
            # Count matches for selected country
            if selected_country in match:
                counter_country.add(match)

        # Count occurences for selected match
        match = [
            qualified_all[select_match].name,
            qualified_all[selected_bracket[select_match]].name,
        ]
        match.sort()
        match = f"{match[0]}-{match[1]}"
        counter_match.add(match)

    with open(f"temp/counter_{index}.pckl", "wb") as f:
        pickle.dump(counter_all, f)
    with open(f"temp/counter_country_{index}.pckl", "wb") as f:
        pickle.dump(counter_country, f)
    with open(f"temp/counter_match_{index}.pckl", "wb") as f:
        pickle.dump(counter_match, f)
    print("End of simulation")


def combine_results(*counters):
    combined = counters[0]
    for counter in counters[1:]:
        combined.append(counter)
    return combined

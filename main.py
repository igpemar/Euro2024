import bracket, simulation, group
import multiprocessing
import pickle
import math

N = 100000
selected_country = "Spain"
select_match = "1B"
display_max = 16
PROCESSES = 20


def worker(N, index):
    counter, counter_country, counter_match = {}, {}, {}
    qualified_directly, qualified_potentially, qualified_all = {}, {}, {}
    total_country_match, total_match = 0, 0
    for i in range(N):
        bracket_string = ""
        print(f"Begin of simulation {i + 1}/{N}, {round((i+1)/N*100,3)}%")
        ## Setup
        groups = group.initialize()

        ## Simulate pending matches
        for g in groups:
            # g.simulate(simulation.random_result)
            g.simulate(simulation.ranking_biased)

        ## Update standings
        for g in groups:
            g.update_standings()

        ## Get direct qualified teams
        for g in groups:
            qualified_directly.update(g.qualifies())

        # Get potentially qualified teams
        for g in groups:
            qualified_potentially.update(g.qualifies([3]))

        # Get teams qualified as thirds
        group_3rd = group.Group("3rd", [])
        group_3rd.teams = {i.name: i for i in qualified_potentially.values()}
        group_3rd.update_standings_3rd_group()
        qualigies_3rd_group = group_3rd.qualifies([1, 2, 3, 4], override_tag=True)

        qualified_all.update(qualified_directly)
        qualified_all.update(qualigies_3rd_group)

        # Generate bracket
        for key in qualigies_3rd_group.keys():
            bracket_string += key[1]

        selected_bracket = bracket.get_bracket_map(bracket_string)

        bracket_list = []
        for Home, Away in selected_bracket.items():
            h_a_sorted = [qualified_all[Home].name, qualified_all[Away].name]
            h_a_sorted.sort()
            bracket_list.append(f"{h_a_sorted[0]}-{h_a_sorted[1]}")

        # Count all matches and for selected country
        for match in bracket_list:
            counter[match] = counter.get(match, 0) + 1
            total_match += 1
            if selected_country in match:
                total_country_match += 1
                counter_country[match] = counter_country.get(match, 0) + 1

        # Count occurences for selected match
        h_a_sorted = [
            qualified_all["1B"].name,
            qualified_all[selected_bracket["1B"]].name,
        ]
        h_a_sorted.sort()
        match = f"{h_a_sorted[0]}-{h_a_sorted[1]}"
        counter_match[match] = counter_match.get(match, 0) + 1

    with open(f"counter_{index}.pckl", "wb") as f:
        pickle.dump(counter, f)
    with open(f"counter_country_{index}.pckl", "wb") as f:
        pickle.dump(counter_country, f)
    with open(f"counter_match_{index}.pckl", "wb") as f:
        pickle.dump(counter_match, f)
    print("End of simulation")


def combine_results(*dicts):
    total_matches = 0
    combined_results = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            if key in combined_results:
                combined_results[key] += value  # If the key exists, add the values
            else:
                combined_results[key] = (
                    value  # If the key doesn't exist, add the key-value pair
                )
            total_matches += value
    return combined_results, total_matches


if __name__ == "__main__":
    counters = {}
    # Create threads
    process = []
    for i in range(PROCESSES):
        process.append(
            multiprocessing.Process(target=worker, args=(math.ceil(N / PROCESSES), i))
        )

    # Start threads
    for i in range(PROCESSES):
        process[i].start()

    # Wait for both threads to finish
    for i in range(PROCESSES):
        process[i].join()

    # Load and combine results
    counter_all = []
    counter_country = []
    counter_matches = []
    for i in range(PROCESSES):
        with open(f"counter_{i}.pckl", "rb") as f:
            counter_all.append(pickle.load(f))
        with open(f"counter_country_{i}.pckl", "rb") as f:
            counter_country.append(pickle.load(f))
        with open(f"counter_match_{i}.pckl", "rb") as f:
            counter_matches.append(pickle.load(f))

    counter, total = combine_results(*counter_all)
    counter_country, total_country = combine_results(*counter_country)
    counter_match, total_matches = combine_results(*counter_matches)
    # Printing results
    print("==================================")
    display = 0
    sorted_counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    for match, count in sorted_counter.items():
        print(f"{match}: {round(100*count/total,2)}%")
        display += 1
        if display >= display_max:
            break

    print("==================================")
    display = 0
    sorted_counter_country = dict(
        sorted(counter_country.items(), key=lambda x: x[1], reverse=True)
    )
    print(f"Matches for {selected_country}")
    for match, count in sorted_counter_country.items():
        print(f"{match}: {round(100*count/total_country,2)}%")
        display += 1
        if display >= display_max:
            break

    print("==================================")
    display = 0
    sorted_counter_match = dict(
        sorted(counter_match.items(), key=lambda x: x[1], reverse=True)
    )
    print(f"Matches for {select_match}")
    for match, count in sorted_counter_match.items():
        print(f"{match}: {round(100*count/total_matches,2)}%")
        display += 1
        if display >= display_max:
            break

    print("==================================")
    print("Checks")
    check, check_country, check_selected_match = 0, 0, 0
    for match, count in sorted_counter.items():
        check += count
    for match, count in sorted_counter_country.items():
        check_country += count
    for match, count in sorted_counter_match.items():
        check_selected_match += count
    print([check, total])
    if check != total:
        raise Exception("All Check failed")
    print([check_country, total_country])
    if check_country != total_country:
        raise Exception("Country Check failed")
    print([check_selected_match, total_matches])
    if check_selected_match != total_matches:
        raise Exception("Selected Match Check failed")

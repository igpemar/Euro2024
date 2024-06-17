import multiprocessing
import calendars, simulation
import pickle
import time

N = 5000
display_max = 24
PROCESSES = 10

if __name__ == "__main__":
    counters = {}
    # Create threads
    process = []
    if PROCESSES < 1:
        raise Exception("N must be >0")
    if N % PROCESSES != 0:
        raise Exception("N must be strictly divisible by PROCESSES")
    t_start = time.time()
    if PROCESSES == 1:
        simulation.worker(N, 0)
    else:
        for i in range(PROCESSES):
            process.append(
                multiprocessing.Process(
                    target=simulation.worker, args=(N / PROCESSES, i)
                )
            )

        # Start threads
        for i in range(PROCESSES):
            process[i].start()

        # Wait for both threads to finish
        for i in range(PROCESSES):
            process[i].join()

    # Load and combine results
    counter_all_lst, counter_country_lst, counter_matches_lst = [], [], []
    for i in range(PROCESSES):
        with open(f"counter_{i}.pckl", "rb") as f:
            counter_all_lst.append(pickle.load(f))
        with open(f"counter_country_{i}.pckl", "rb") as f:
            counter_country_lst.append(pickle.load(f))
        with open(f"counter_match_{i}.pckl", "rb") as f:
            counter_matches_lst.append(pickle.load(f))

    counter_all = simulation.combine_results(*counter_all_lst)
    counter_country = simulation.combine_results(*counter_country_lst)
    counter_match = simulation.combine_results(*counter_matches_lst)
    t_end = time.time()
    with open(f"counter_all_{N}_G{calendars.G}.pckl", "wb") as f:
        pickle.dump(counter_all, f)
    # Printing results
    print("==================================")
    display = 0
    counter_all.sort()
    print(f"{len(counter_all.count)} possible games calculated")
    for match, count in counter_all.count.items():
        print(f"{match}: {round(100*count/counter_all.total,2)}%")
        display += 1
        if display >= display_max:
            break

    print("==================================")
    display = 0
    counter_country.sort()
    print(f"Matches for {simulation.selected_country}")
    for match, count in counter_country.count.items():
        print(f"{match}: {round(100*count/counter_country.total,2)}%")
        display += 1
        if display >= display_max:
            break

    print("==================================")
    display = 0
    print(f"Matches for {simulation.select_match}")
    counter_match.sort()
    for match, count in counter_match.count.items():
        print(f"{match}: {round(100*count/counter_match.total,2)}%")
        display += 1
        if display >= display_max:
            break

    print("==================================")
    print("Checks")
    check, check_country, check_selected_match = 0, 0, 0
    for match, count in counter_all.count.items():
        check += count
    for match, count in counter_country.count.items():
        check_country += count
    for match, count in counter_match.count.items():
        check_selected_match += count
    print([check, 8 * N])
    if check != 8 * N:
        raise Exception("All Check failed")
    print([check_selected_match, N])
    if check_selected_match != N:
        raise Exception("Selected Match Check failed")

    elapsed = t_end - t_start
    print(f"Elapsed time: {round(elapsed,2)} seconds")
import matplotlib.pyplot as plt
import pickle
import simulation
import numpy as np

source_file = "counter_all_1000_G0.pckl"

# List of country names
with open(source_file, "rb") as f:
    counter_all = pickle.load(f)
countries = set()

countries = sorted(list(simulation.fifa_ranking.keys()))
country_indices = {}
for i, country in enumerate(countries):
    country_indices[country] = i


data = np.zeros([len(countries), len(countries)])
for game, count in counter_all.count.items():
    i = country_indices[game.split("-")[0]]
    j = country_indices[game.split("-")[1]]
    data[i][j] = count
    data[j][i] = count

for i in range(data.shape[0]):
    row_sum = np.sum(data[i, :])  # Sum of the elements in the row
    if row_sum != 0:  # To avoid division by zero
        data[i, :] = 100 * data[i, :] / row_sum

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
cax = ax.matshow(data, cmap="coolwarm")

# Add color bar
fig.colorbar(cax)

# Loop over data dimensions and create text annotations.
for i in range(len(data)):
    for j in range(len(data[i])):
        ax.text(
            j,
            i,
            f"{round(data[i][j],1)}",
            ha="center",
            va="center",
            color="black",
            fontsize=8,
        )

# Set axis labels with country names
ax.set_xticks(range(len(countries)))
ax.set_yticks(range(len(countries)))
ax.set_xticklabels(countries)
ax.set_yticklabels(countries)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Set title
plt.title([source_file, "Round of 16 Match Probabilities"])

# Display the plot
plt.show()

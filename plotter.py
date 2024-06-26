import matplotlib.pyplot as plt
import pickle
import simulation
import numpy as np

MODE = "FR"


def plot(G: int, N: int) -> None:
    for n in range(G, G + 1):
        source_file = f"{MODE}/counter_all_{N}_G{n}.pckl"

        # List of country names
        with open(source_file, "rb") as f:
            counter_all = pickle.load(f)
        countries = set()

        countries = sorted(list(simulation.fifa_ranking.keys()))
        country_indices = {}
        for i, country in enumerate(countries):
            country_indices[country] = i

        data = np.zeros([len(countries), len(countries) + 1])
        for game, count in counter_all.count.items():
            i = country_indices[game.split("-")[0]]
            j = country_indices[game.split("-")[1]]
            data[i][j] = count
            data[j][i] = count

        all_games = np.sum(data)
        print(all_games)
        for i in range(data.shape[0]):
            # row_sum = np.sum(data[i, :])  # Sum of the elements in the row
            data[i, :] = 100 * data[i, :] / (all_games / 16)
            # data[i, -1] = str(100 * row_sum / (all_games / 16))

        # Create the plot
        vmin = 0
        vmax = np.max(
            data[:, :-1]
        )  # You can set this to the maximum value you want for the colormap
        print(vmax)
        fig, ax = plt.subplots(figsize=(16, 10))
        cax = ax.matshow(data, cmap="coolwarm", vmin=vmin, vmax=vmax / 2)

        # Add color bar
        cbar = fig.colorbar(cax)
        cbar.set_label("Probability (%)")
        # fig.colorbar(cax)
        for i in range(data.shape[0]):
            row_sum = np.sum(data[i, :])  # Sum of the elements in the row
            data[i, -1] = row_sum

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
        ax.set_xticks(range(len(countries) + 1))
        ax.set_yticks(range(len(countries)))
        ax.set_xticklabels(countries + ["Total"], fontsize=10)
        ax.set_yticklabels(countries, fontsize=11)

        # Rotate the x-axis labels for better readability
        plt.xticks(rotation=90)

        # Set title
        plt.title(
            f"Round of 16 Match Probabilities; Game Day {n}; N = {N:,}",
        )

        # Display the plot
        plt.savefig(f"plots/{MODE}_N_{N}_G{n}.png", dpi=500)

        plt.show()


if __name__ == "__main__":
    plot()

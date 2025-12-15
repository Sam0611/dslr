import sys
import matplotlib.pyplot as plt
import pandas as pd

from utils import get_label, get_numerical_data, init_subplots


def pair_plot():
    if len(sys.argv) != 2:
        raise Exception("One argument is required : the path to csv file")

    # get data from csv file
    data = pd.read_csv(sys.argv[1])
    num_data = get_numerical_data(data)

    # init variables
    houses_names = data["Hogwarts House"].unique()
    colors = ['blue', 'green', 'red', 'yellow', 'orange']
    num_features = len(num_data.columns)

    # init subplots
    axes = init_subplots(num_features ** 2, num_features, num_features)

    for row in range(num_features):
        for col in range(num_features):
            name1 = num_data.columns[row]
            name2 = num_data.columns[col]

            c = 0
            for house in houses_names:
                if len(houses_names) <= 1:  # Hogwarts House = nan
                    c = 4
                    tmp_data = num_data
                else:
                    tmp_data = num_data[data['Hogwarts House'].isin([house])]

                if row == col:
                    axes[row, col].hist(
                        tmp_data[name1],
                        bins=15,
                        color=colors[c],
                        alpha=0.6
                    )
                else:
                    axes[row, col].scatter(
                        tmp_data[name1],
                        tmp_data[name2],
                        color=colors[c],
                        alpha=0.6,
                        s=1
                    )
                c = c + 1

            if col == 0:
                axes[row, col].set_ylabel(get_label(name1, 10), fontsize=8)
            if row == num_features - 1:
                axes[row, col].set_xlabel(get_label(name2, 15), fontsize=8)

            axes[row, col].set_xticks([])
            axes[row, col].set_yticks([])

    plt.tight_layout()
    plt.show()


def main():
    try:
        pair_plot()
    except Exception as error:
        print("Error:", error)


if (__name__ == "__main__"):
    main()

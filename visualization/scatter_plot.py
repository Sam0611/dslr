import sys
import math
import matplotlib.pyplot as plt
import pandas as pd

from utils import get_not_empty_values, get_label, press, get_numerical_data, init_subplots

def get_subplots_params(num_features):

    # calculate number of graph
    n_plots = 0
    for i in range(num_features):
        n_plots = n_plots + i

    # calculate number of rows and columns
    nrows = round(n_plots ** 0.5)
    ncols = math.ceil(n_plots ** 0.5)

    return n_plots, nrows, ncols


def scatter_plot():
    if len(sys.argv) != 2:
        raise Exception("One argument is required : the path to csv file")
    
    # get data from csv file
    data = pd.read_csv(sys.argv[1])
    num_data = get_numerical_data(data)

    # init variables
    houses_names = data["Hogwarts House"].unique()
    colors = ['blue', 'green', 'red', 'yellow', 'orange']
    num_features = len(num_data.columns)
    n_plots, nrows, ncols = get_subplots_params(num_features)

    # init subplots
    axes = init_subplots(n_plots, nrows, ncols)

    row = 0
    col = 0
    for i in range(num_features - 1):
        for j in range(i + 1, num_features):
            name1 = num_data.columns[i]
            name2 = num_data.columns[j]

            if col >= ncols:
                col = 0
                row = row + 1

            c = 0
            for house in houses_names:
                if len(houses_names) <= 1: # Hogwarts House = nan
                    c = 4
                    tmp_data = num_data
                else:
                    tmp_data = num_data[data['Hogwarts House'].isin([house])]

                axes[row, col].scatter(
                    tmp_data[name1],
                    tmp_data[name2],
                    color=colors[c],
                    alpha=0.6,
                    s=1
                )
                c = c + 1

            axes[row, col].set_ylabel(get_label(name1, 10), fontsize=8)
            axes[row, col].set_xlabel(get_label(name2, 15), fontsize=8)

            axes[row, col].set_xticks([])
            axes[row, col].set_yticks([])

            col = col + 1

    plt.tight_layout()
    plt.show()


def main():
    try:
        scatter_plot()
    except Exception as error:
        print("Error:", error)


if (__name__ == "__main__"):
    main()

import sys
import math
import matplotlib.pyplot as plt
import pandas as pd

from utils import get_numerical_data, init_subplots


def histogram(data):
    """Display numerical data as histogram"""

    num_data = get_numerical_data(data)

    # init variables
    houses_names = data["Hogwarts House"].unique()
    colors = ['blue', 'green', 'red', 'yellow', 'orange']
    num_features = len(num_data.columns)
    nrows = round(num_features ** 0.5)
    ncols = math.ceil(num_features ** 0.5)

    # init subplots
    axes = init_subplots(num_features, nrows, ncols)

    col = 0
    row = 0
    for name in num_data.columns:
        if (col >= ncols):
            col = 0
            row = row + 1

        c = 0
        for house in houses_names:
            if len(houses_names) <= 1:  # Hogwarts House = nan
                c = 4
                tmp_data = num_data
            else:
                tmp_data = num_data[data['Hogwarts House'].isin([house])]

            axes[row, col].hist(
                tmp_data[name],
                bins=30,
                color=colors[c],
                alpha=0.6
            )
            axes[row, col].set_title(name)
            c = c + 1

        col = col + 1

    plt.tight_layout()
    plt.show()


def main():
    try:
        data = pd.read_csv(sys.argv[1])
        histogram(data)
    except IndexError:
        print('One argument is required : the path to csv file')
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

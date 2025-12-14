import sys
import math
import matplotlib.pyplot as plt
import pandas as pd


def get_not_empty_values(args: any):
    """returns every not empty values"""
    values = []
    for data in args:
        if data == data:
            values.append(data)
    return values


def get_label(str, length):
    if len(str) <= length:
        return str

    label = str[:length].rsplit(" ", 1)
    label = '\n'.join(label) + get_label(str[length:], length)
    return label


def press(event):
    if event.key == "escape":
        plt.close()


def scatter_plot():
    try:
        if len(sys.argv) != 2:
            raise Exception("One argument is required : the path to csv file")
        
        data = pd.read_csv(sys.argv[1])
        num_data = data.select_dtypes(include=['number'])
        num_data = num_data.drop("Index", axis='columns')
        if "Hogwarts House" in num_data.columns:
            num_data = num_data.drop("Hogwarts House", axis='columns')

        hogwarts_houses = data["Hogwarts House"].unique()
        colors = ['blue', 'green', 'red', 'yellow', 'orange']
        num_features = len(num_data.columns)

        n_plots = 0
        for i in range(num_features):
            n_plots = n_plots + i

        nrows = round(n_plots ** 0.5)
        ncols = math.ceil(n_plots ** 0.5)

        fig, axes = plt.subplots(
            nrows=nrows,
            ncols=ncols,
            figsize=(10, 10)
        )

        row = 0
        col = 0
        for i in range(num_features - 1):
            for j in range(i + 1, num_features):
                if col >= ncols:
                    col = 0
                    row = row + 1
                name1 = num_data.columns[i]
                name2 = num_data.columns[j]

                c = 0
                for house in hogwarts_houses:
                    if len(hogwarts_houses) <= 1:
                        c = 4
                        tmp_data = num_data
                    else:
                        tmp_data = num_data[data['Hogwarts House'].isin([house])]

                    axes[row, col].scatter(
                        tmp_data[name1],
                        tmp_data[name2],
                        color=colors[c],
                        s=1
                    )
                    c = c + 1

                axes[row, col].set_ylabel(get_label(name1, 10), fontsize=8)
                axes[row, col].set_xlabel(get_label(name2, 15), fontsize=8)

                axes[row, col].set_xticks([])
                axes[row, col].set_yticks([])

                col = col + 1

        for i in range(nrows * ncols - n_plots):
            axes[row, col + i].set_visible(False)

        plt.tight_layout()
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        _ = fig.canvas.mpl_connect('key_press_event', press)
        plt.show()

    except Exception as error:
        print("Error:", error)


def main():
    scatter_plot()


if (__name__ == "__main__"):
    main()

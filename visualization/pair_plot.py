import sys
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


def pair_plot():
    try:
        if len(sys.argv) != 2:
            raise Exception("One argument is required : the path to csv file")

        data = pd.read_csv(sys.argv[1])

        num_data = data.select_dtypes(include=['number'])
        num_data = num_data.drop("Index", axis='columns')
        if "Hogwarts House" in num_data.columns:
            num_data = num_data.drop("Hogwarts House", axis='columns')

        num_features = len(num_data.columns)

        fig, axes = plt.subplots(
            nrows=num_features,
            ncols=num_features,
            figsize=(10, 10)
        )

        for i in range(num_features):
            for j in range(num_features):
                name1 = num_data.columns[i]
                name2 = num_data.columns[j]
                if i == j:
                    axes[i, j].hist(
                        num_data[name1],
                        bins=15,
                        color='pink',
                        edgecolor='black'
                    )
                else:
                    axes[i, j].scatter(
                        num_data[name1],
                        num_data[name2],
                        color='orange',
                        s=1
                    )

                if j == 0:
                    axes[i, j].set_ylabel(get_label(name1, 10), fontsize=8)
                if i == num_features - 1:
                    axes[i, j].set_xlabel(get_label(name2, 15), fontsize=8)

                axes[i, j].set_xticks([])
                axes[i, j].set_yticks([])

        plt.tight_layout()
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        _ = fig.canvas.mpl_connect('key_press_event', press)
        plt.show()

    except Exception as error:
        print("Error:", error)


def main():
    pair_plot()


if (__name__ == "__main__"):
    main()

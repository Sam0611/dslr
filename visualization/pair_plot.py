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


def pair_plot():
    try:
        if len(sys.argv) != 2:
            raise Exception("One argument is required : the path to csv file")
        
        data = pd.read_csv(sys.argv[1])

        numerical_data = data.select_dtypes(include=['number'])
        numerical_data = numerical_data.drop("Index", axis='columns')
        if "Hogwarts House" in numerical_data.columns:
            numerical_data = numerical_data.drop("Hogwarts House", axis='columns')

        num_features = len(numerical_data.columns)

        fig, axes = plt.subplots(nrows=num_features, ncols=num_features, figsize=(10, 10))

        for i in range(num_features):
            for j in range(num_features):
                name1 = numerical_data.columns[i]
                name2 = numerical_data.columns[j]
                if i == j:
                    axes[i, j].hist(numerical_data[name1], bins=15, color='Yellow', edgecolor='black')
                else:
                    axes[i, j].scatter(numerical_data[name1], numerical_data[name2], color='blue')

                if j == 0:
                    axes[i, j].set_ylabel(name1)
                if i == num_features - 1:
                    axes[i, j].set_xlabel(name2, fontsize=10)

                axes[i, j].set_xticks([])
                axes[i, j].set_yticks([])

        plt.tight_layout()
        plt.show()

    except Exception as error:
        print("Error:", error)


def main():
    pair_plot()


if (__name__ == "__main__"):
    main()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import statistics


def main():
    try:
        if len(sys.argv) != 2:
            raise Exception("One argument is required : the path to csv file")

        data = pd.read_csv(sys.argv[1])
        numerical_data = data.select_dtypes(include=['number'])
        numerical_data = numerical_data.drop("Index", axis='columns')

        fig, axes = plt.subplots(nrows=3, ncols=5, figsize=(12, 4))

        i = 0
        j = 0
        for name in numerical_data.columns:
            axes[j, i].hist(numerical_data[name], bins=30, color='Yellow', edgecolor='black')
            axes[j, i].set_title(name)
            i = i + 1
            if (i >= 5):
                j = j + 1
                i = 0

        plt.show()

        # for name in numerical_data.columns:
        #     plt.hist(numerical_data[name])
        #     plt.title(name)
        #     plt.show()

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
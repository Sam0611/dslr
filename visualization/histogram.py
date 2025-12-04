import sys
sys.path.append("../")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from analysis import statistics

def get_not_empty_values(args: any):
    """returns every not empty values"""
    values = []
    for data in args:
        if data == data:
            values.append(data)
    return values

def main():
    try:
        if len(sys.argv) != 2:
            raise Exception("One argument is required : the path to csv file")

        data = pd.read_csv(sys.argv[1])
        numerical_data = data.select_dtypes(include=['number'])
        numerical_data = numerical_data.drop("Index", axis='columns')
        numerical_data = numerical_data.drop("Hogwarts House", axis='columns')

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

        # add histogram of variance
        std = []
        for name in numerical_data.columns:
            col = get_not_empty_values(numerical_data[name])
            std.append(statistics.get_standard_deviation(col))
        # print(std)
        plt.hist(std)

        # axes[j, i].hist()

        plt.show()

        # for name in numerical_data.columns:
        #     plt.hist(numerical_data[name])
        #     plt.title(name)
        #     plt.show()

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
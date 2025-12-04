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
        numerical_data = numerical_data.drop("Hogwarts House", axis='columns')

        graph_nbrs = 144
        graph_cols = 12
        fig, axes = plt.subplots(nrows=12, ncols=12, figsize=(graph_nbrs, graph_cols))
        print("tewst") 

        i = 0
        j = 0
        for name in numerical_data.columns:
            axes[j, i].hist(numerical_data[name], bins=30, color='Yellow', edgecolor='black')
            axes[j, i].set_title(name)
            i = i + 1
            if (i >= graph_cols):
                j = j + 1
                i = 0

        axes[j, i].hist()

        plt.show()

        # for x in numerical_data:
        #     col = numerical_data[x]
        #     plt.pair(col, newAges)
        #     plt.show()



        plt.scatter(col1, col2)
        plt.show()

    except Exception as error:
        print("Error:", error)


def main():
    pair_plot()


if (__name__ == "__main__"):
    main()
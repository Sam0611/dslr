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


def scatter_plot():
    try:
        if len(sys.argv) != 2:
            raise Exception("One argument is required : the path to csv file")
        data = pd.read_csv(sys.argv[1])
        numerical_data = data.select_dtypes(include=['number'])
        numerical_data = numerical_data.drop("Index", axis='columns')
        numerical_data = numerical_data.drop("Hogwarts House", axis='columns')

        col1 = numerical_data['Arithmancy']
        col2 = data['Astronomy']

        # for x in numerical_data:
        #     col = numerical_data[x]
        #     plt.scatter(col, newAges)
        #     plt.show()



        plt.scatter(col1, col2)
        plt.show()

    except Exception as error:
        print("Error:", error)


def main():
    scatter_plot()


if (__name__ == "__main__"):
    main()
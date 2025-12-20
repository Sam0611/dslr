import sys
import pandas as pd
import numpy as np

from utils import get_probabilities


def logreg_predict(data, weight_file):
    """
        takes a dataset as first parameter
        and the name of the file containing the weights
        generates a prediction file 'houses.csv'
    """

    # get numerical data only
    num_data = data.select_dtypes(include=['number'])
    num_data = num_data.drop("Index", axis='columns')
    if "Hogwarts House" in num_data.columns:
        num_data = num_data.drop("Hogwarts House", axis='columns')

    # replace nan values with the mean
    for col in num_data.columns:
        num_data.fillna({col: num_data[col].mean()}, inplace=True)

    # normalize data with Z-Score method
    for col in num_data.columns:
        num_data[col] = num_data[col] - num_data[col].mean()
        num_data[col] = num_data[col] / num_data[col].std()

    # add column of one
    num_data.insert(0, 'x0', np.ones(len(num_data)))

    # read file containing weights and calculate probabilities
    p = get_proba_from_file(weight_file, num_data)

    # write prediction file
    f = open('houses.csv', 'w')
    f.write("Index,Hogwarts House\n")
    for row in range(len(p)):
        house = p.columns[0]
        for col in p.columns:
            if p.loc[row, col] > p.loc[row, house]:
                house = col
        f.write(f"{row},{house}\n")
    f.close()


def get_proba_from_file(filename, data):
    """
        Read file passed as first argument
        and get every weight values for each house
        Returns probabilies for each student to belong to each house
        using weight values
    """
    p = {}
    values = []
    label = ''
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if line.isalpha():
                if len(label) > 0:
                    p[label] = get_probabilities(data, values)
                    values.clear()
                label = line
            else:
                values.append(float(line))
    p[label] = get_probabilities(data, values)
    return pd.DataFrame(p)


def main():
    try:
        data = pd.read_csv(sys.argv[1])
        logreg_predict(data, sys.argv[2])
    except IndexError:
        print(
            "Two arguments are required : "
            "the path to csv file and file containing the weights"
        )
    except Exception as error:
        print("Error:", error)


if (__name__ == "__main__"):
    main()

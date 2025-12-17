import sys
import math
import pandas as pd
import numpy as np


def replace_nan_values(data, num_data):
    for col in num_data.columns:
        for i in range(len(num_data[col])):
            if math.isnan(num_data[col].loc[i]):
                house = data.loc[i, 'Hogwarts House']
                tmp_data = num_data[data['Hogwarts House'].isin([house])]
                num_data.loc[i, col] = tmp_data[col].mean()


def logreg_train():
    """
        takes dataset_train.csv as a parameter
        generates a file containing the weights
        that will be used for the prediction
    """
    if len(sys.argv) != 2:
        raise Exception("One argument is required : the path to csv file")

    # get data from csv file
    data = pd.read_csv(sys.argv[1])
    num_data = data.select_dtypes(include=['number'])
    num_data = num_data.drop("Index", axis='columns')

    # replace nan values with the mean for same house
    replace_nan_values(data, num_data)

    # init variables
    n_rows = len(data['Index'])
    n_cols = len(num_data.columns) + 1
    weights = np.zeros(n_cols)
    p = np.array([])

    # add column of one
    num_data.insert(0, 'x0', np.ones(n_rows))

    # y = 0|1
    y = np.where(data['Hogwarts House'] == 'Gryffindor', 1, 0)

    # z = w0 + x1*w1 + xn*wn
    for i in range(n_rows):
        row = np.array(num_data.loc[i])
        z = 0
        for j in range(len(row)):
            z = z + weights[j] * row[j]

        # p = 1 / (1 + e(-z))
        p = np.append(p, 1 / (1 + math.exp(-z)))

    # gradient_descent = 1/n * X'(p - y)
    for col in range(n_cols):
        gd = 0
        x = np.array(num_data[num_data.columns[col]])
        for row in range(n_rows):
            gd = gd + x[row] * (p[row] - y[row])
        gd = gd / n_rows

        # w = w - 0.1 * gd
        weights[col] = weights[col] - 0.1 * gd

    # loss fct L = -1/n * ( y*log(p) + (1 - y)*log(1 - p) )
    L = -1 / n_rows * (y[0] * math.log(p[0]) + (1 - y[0]) * math.log(1 - p[0]))


def main():
    try:
        logreg_train()
    except Exception as error:
        print("Error:", error)


if (__name__ == "__main__"):
    main()

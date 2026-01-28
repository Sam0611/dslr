import sys
import math
import pandas as pd
import numpy as np

from utils import get_probabilities


def replace_nan_values(data, num_data):
    """
        Replaces nan values of num_data
        with the mean of the corresponding house
    """
    for col in num_data.columns:
        for i in range(len(num_data[col])):
            if math.isnan(num_data[col].loc[i]):
                house = data.loc[i, 'Hogwarts House']
                tmp_data = num_data[data['Hogwarts House'].isin([house])]
                num_data.loc[i, col] = tmp_data[col].mean()


def logreg_train(data):
    """
        takes dataset_train.csv as a parameter
        generates a file containing the weights
        that will be used for the prediction
    """

    # get numerical data only
    num_data = data.select_dtypes(include=['number'])
    num_data = num_data.drop("Index", axis='columns')

    replace_nan_values(data, num_data)

    # normalize data with Z-Score method
    for col in num_data.columns:
        num_data[col] = num_data[col] - num_data[col].mean()
        num_data[col] = num_data[col] / num_data[col].std()

    # add column of one
    num_data.insert(0, 'x0', np.ones(len(num_data)))

    # get houses name
    houses = data["Hogwarts House"].unique()

    # set colors for each house
    # colors = ['blue', 'green', 'red', 'yellow']
    colors = [96, 92, 91, 93]

    f = open('weights.txt', 'w')
    for i in range(len(houses)):
        # y = 1 if is the right house, 0 if not
        y = np.where(data['Hogwarts House'] == houses[i], 1, 0)

        print(f"\033[{colors[i]};1m{houses[i]}")

        # init weights at 0
        weights = np.zeros(len(num_data.columns))

        # init probabilities
        p = get_probabilities(num_data, weights)

        loss = 1
        count = 0
        while loss > 0.1:

            # update weights
            gradient_descent(num_data, weights, p, y)

            # get probability for each row
            p = get_probabilities(num_data, weights)

            # calculates how far from true probabilities
            loss = get_loss_value(y, p)

            print(loss, end="\r")
            count = count + 1

        print_results(data, p, count, loss, houses[i])

        print('\033[00;1m------------------------------------\033[00m')

        # write weight values in file
        f.write(f"{houses[i]}\n")
        for w in weights:
            f.write(f"{w}\n")
    f.close()


def print_results(data, p, count, loss, house):
    """Displays number of iterations and errors"""
    fp = 0
    fn = 0
    for i in range(len(p)):
        if p[i] > 0.5 and data.loc[i, 'Hogwarts House'] != house:
            fp = fp + 1
        if p[i] < 0.5 and data.loc[i, 'Hogwarts House'] == house:
            fn = fn + 1

    print('Number of iterations :', count)
    print('Loss value :', loss)
    print('Number of false positive :', fp)
    print('Number of false negative :', fn)
    print('Total of false predictions :', fp + fn)


def gradient_descent(num_data, weights, p, y):
    """
        Update the weights using gradient descent
        w = w - 0.1 * gd
        gd = mean(x[i] * (p[i] - y[i]))
    """
    n_cols = len(num_data.columns)
    n_rows = len(num_data)
    for col in range(n_cols):
        gd = 0
        x = np.array(num_data[num_data.columns[col]])
        for row in range(n_rows):
            gd = gd + x[row] * (p[row] - y[row])
        gd = gd / n_rows
        weights[col] = weights[col] - 0.1 * gd


def get_loss_value(y, p):
    """returns the mean of y*log(p) + (1 - y)*log(1 - p)"""
    loss = 0
    n = len(y)
    for i in range(n):
        loss = loss + (y[i] * math.log(p[i]) + (1 - y[i]) * math.log(1 - p[i]))
    loss = loss / -n
    return loss


def main():
    try:
        data = pd.read_csv(sys.argv[1])
        logreg_train(data)
    except IndexError:
        print('One argument is required : the path to csv file')
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

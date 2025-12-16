import sys
import math
import pandas as pd
import numpy as np


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
    # df['A'].fillna(df['A'].mean(), inplace=True)

    # init variables
    n_rows = len(data['Index'])
    n_cols = len(num_data.columns)
    weights = np.zeros(n_cols + 1)

    # y = 0|1
    houses = np.where(data['Hogwarts House'] == 'Gryffindor', 1, 0)

    h = np.array([])

    # xw = w0 + x1*w1 + xn*wn
    x = np.array(num_data.loc[0])

    xw = weights[0]
    for i in range(len(x)):
        xw = xw + weights[i + 1] * x[i]

    # h = 1 / (1 + e(-xw))
    h = np.append(h, 1 / (1 + math.exp(-xw)))
    
    print(len(h))

    # gradient_descent = 1/n * X'(h - y)

    # gd1 = 1/n * (h0 - y0 + hn - yn)
    # gd2 = 1/n * ((h0 - y0) * x0 + (hn - yn) * xn)
    gradient_descent = h[0]
    gradient_descent = gradient_descent / n_rows

    # weights = weights - 0.1 * gradient_descent


    # loss fct L = -1/n * ( y*log(h) + (1 - y)*log(1 - h) )


def main():
    try:
        logreg_train()
    except Exception as error:
        print("Error:", error)


if (__name__ == "__main__"):
    main()

import numpy as np
import pandas as pd
import data_parsing


def compare_lr_results(data_csv, houses_csv):
    houses = data_parsing.get_student_houses(data_csv)
    predics = pd.read_csv(houses_csv)['Hogwarts House']

    accuracy = (houses == predics)
    good_results = accuracy[accuracy == True].size
    false_results = accuracy[accuracy == False].size
    print(f"Accuracy = {good_results * 100 / accuracy.size}%, (True : {good_results}, False : {false_results})")


def normalise_data(data):
    '''proportional normalisation in poucentage (x/100)'''
    # i = data.shape[1] - 1
    # while i >= 0:
    #     max = np.max(data[:, i])
    #     min = np.min(data[:, i])
    #     range = abs(max - min)
    #     data[:, i] -= min
    #     data[:, i] = data[:, i] * 100 / range
    #     i -= 1
    # return (data)

    # normalize data with Z-Score method
    i = data.shape[1] - 1
    while i >= 0:
        data[:, i] = data[:, i] - data[:, i].mean()
        data[:, i] = data[:, i] / data[:, i].std()
        i -= 1
    return data

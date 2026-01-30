import pandas as pd
import numpy as np
from typing import Callable


def normalise_data(data: np.ndarray) -> np.ndarray:
    '''proportional normalisation in poucentage (x/1)'''
    for i in range(data.shape[1]):
        max = np.max(data[:, i])
        min = np.min(data[:, i])
        spread = abs(max - min)
        data[:, i] -= min
        data[:, i] = data[:, i] * 1 / spread
    return (data)


def hogwarts_house_to_value(data, hogwarts_house_dict):
    my_result = data['Hogwarts House'].map(hogwarts_house_dict)
    return (my_result)


def pandas_remove_nan_line(data):
    return (data[~data.isnull().any(axis=1) == True])


def replace_nan_value_by_0(data):
    positions = np.argwhere(data.isna().to_numpy())
    for i in positions:
        data.iloc[i[0], i[1]] = 0
    return data


def replace_nan_value(data):
    house_average = pandas_get_house_average(data)

    hogwarts_house_names_dict = {"Gryffindor": 0, "Slytherin": 1, "Hufflepuff": 2, "Ravenclaw": 3}
    positions = np.argwhere(data.isna().to_numpy())
    for i in positions:
        house_of_instance = data.loc[i[0], 'Hogwarts House']
        right_house_average = house_average[hogwarts_house_names_dict[house_of_instance]]
        data.iloc[i[0], i[1]] = right_house_average.iloc[i[1]]

    return data


def get_students_scores(data_csv, treat_nan_values: Callable = replace_nan_value_by_0):
    ''' parameter 1 : name of the data.csv file
        parameter 2 : (optional) name of the function used to treat nan values
        Return X : the score of each feature per index '''

    X = pd.read_csv(data_csv)
    X.drop(['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'], axis=1, inplace=True)
    X = treat_nan_values(X)
    X.drop('Hogwarts House', axis=1, inplace=True)
    X = X.to_numpy(dtype=np.float64)
    normalise_data(X)
    return X


def get_students_scores_predict(data_csv, thetas, treat_nan_values: Callable = replace_nan_value_by_0):
    ''' parameter 1 : name of the data.csv file
        parameter 2 : (optional) name of the function used to treat nan values
        Return X : the score of each feature per index '''

    X = pd.read_csv(data_csv)
    X.drop(['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'], axis=1, inplace=True)

    # check if features order is the same
    thetas.set_index('Features', inplace=True)
    thetas_labels = list(thetas.index.values)
    X_columns = list(X.columns)
    if (thetas_labels[1:] != X_columns[1:]):
        X = X[['Hogwarts House', thetas_labels[1], thetas_labels[2], thetas_labels[3], thetas_labels[4], thetas_labels[5], thetas_labels[6], thetas_labels[7], thetas_labels[8], thetas_labels[9], thetas_labels[10], thetas_labels[11], thetas_labels[12], thetas_labels[13]]]


    X = treat_nan_values(X)
    X.drop('Hogwarts House', axis=1, inplace=True)
    X = X.to_numpy(dtype=np.float64)
    normalise_data(X)
    return X


def get_student_houses(data_csv, treat_nan_values: Callable = replace_nan_value_by_0):
    y = pd.read_csv(data_csv)
    if (treat_nan_values == pandas_remove_nan_line):
        y = pandas_remove_nan_line(y)
    y = y['Hogwarts House']
    return y


def get_feature_labels(data_csv):
    feature_labels = pd.read_csv(data_csv)
    feature_labels.drop(['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand', 'Hogwarts House'], axis=1, inplace=True)
    feature_labels = list(feature_labels.columns.values)
    feature_labels.insert(0, 'Bias')
    return(feature_labels)



def pandas_get_house_average(data):
    hogwarts_house_names_list = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    house_average = list(range(len(hogwarts_house_names_list)))
    data_no_nan = pandas_remove_nan_line(data)

    for i in range(len(hogwarts_house_names_list)):
        house_notes = data_no_nan[data_no_nan['Hogwarts House'] == hogwarts_house_names_list[i]].copy()
        house_notes.drop('Hogwarts House', axis=1, inplace=True)
        house_average[i] = house_notes.sum() / len(house_notes)

    return house_average

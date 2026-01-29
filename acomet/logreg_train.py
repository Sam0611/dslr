import numpy as np
import pandas as pd
import sys
import data_parsing


def print_results(data, p, count, loss, house):
    """Displays number of iterations and errors"""
    fp = 0
    fn = 0
    for i in range(len(p)):
        if p[i] > 0.5 and data[i] != house:
            fp = fp + 1
        if p[i] < 0.5 and data[i] == house:
            fn = fn + 1

    # set colors for each house [91: red, 92: green, 93: yellow, 96: blue]
    colors = {"Gryffindor": 91, "Slytherin": 92, "Hufflepuff": 93, "Ravenclaw": 96}

    print(f"\033[{colors[house]};1m{house}")
    print('Number of iterations :', count)
    print('Loss value :', loss)
    print('Number of false positive :', fp)
    print('Number of false negative :', fn)
    print('Total of false predictions :', fp + fn)

    print('\033[00;1m------------------------------------\033[00m')


def cost_function(theta, X, y):
    predictions = sigmoid(X @ theta)
    # protect from log(0) = -inf that cause warning
    eps = 1e-15
    predictions = np.clip(predictions, eps, 1 - eps)
    cost = (np.log(predictions) * y) + (np.log(1 - predictions) * (1 - y))
    return (-sum(cost) / y.size)


def sigmoid(z):
    return (1.0 / (1.0 + np.exp(-z)))


def calculate_gradient(theta, X, y):
    return (X.T @ (sigmoid(X @ theta) - y) / y.size)  # derivative


def gradient_descent(X_b, y, alpha=0.001, iter=1000):
    theta = np.zeros(X_b.shape[1])

    for i in range(iter):
        grad = calculate_gradient(theta, X_b, y)
        theta -= alpha * grad

    return theta


def mini_batch_gradient_descent(X_b, y, alpha=0.001, iter=1000, batch_size=10):
    if (batch_size > len(X_b)):
        batch_size = len(X_b)
    theta = np.zeros(X_b.shape[1])
    rng = np.random.default_rng()

    for i in range(iter):
        batch_X_b = rng.choice(X_b.shape[0], size=batch_size, replace=False)
        grad = calculate_gradient(theta, X_b[batch_X_b], y[batch_X_b])
        theta -= alpha * grad

    return theta


def logreg_train(data_csv, parsing_method=data_parsing.replace_nan_value_by_0, alpha=0.01, iter=1000, batch_size=0):
    X = data_parsing.get_students_scores(data_csv, parsing_method)
    X_b = np.c_[np.ones(X.shape[0]), X]    # add intercept (or bias)
    y = data_parsing.get_student_houses(data_csv, parsing_method)

    hogwarts_house_dict = {0: "Gryffindor", 1: "Slytherin", 2: "Hufflepuff", 3: "Ravenclaw"}
    thetas = pd.DataFrame()

    for i in range(len(hogwarts_house_dict)):
        binomial_results = y.copy()
        binomial_results[binomial_results != hogwarts_house_dict[i]] = 0
        binomial_results[binomial_results == hogwarts_house_dict[i]] = 1
        binomial_results = binomial_results.to_numpy(dtype=np.float64)
        if (batch_size > 0):
            thetas[hogwarts_house_dict[i]] = mini_batch_gradient_descent(X_b, binomial_results, alpha, iter, batch_size)
        else:
            thetas[hogwarts_house_dict[i]] = gradient_descent(X_b, binomial_results, alpha, iter)

        print_results(y, sigmoid(X_b @ thetas[hogwarts_house_dict[i]]), iter, cost_function(thetas[hogwarts_house_dict[i]], X_b, binomial_results), hogwarts_house_dict[i])

    thetas.index = data_parsing.get_feature_labels(data_csv)
    thetas.index.name = 'Features'
    thetas.to_csv('weights.csv', index=True)


def logreg_train_parse_args():
    args_dic = {'data_csv=': "dataset_train.csv", 'iter=': "1000", 'alpha=': "0.001", 'parse_method=': 'replace_nan_value_by_0', 'batch_size=': '0'}

    if (len(sys.argv) > 6):
        print("Error to many argument, 6 maximum")
        return

    i = 1
    while (i < len(sys.argv)):
        args_dic[list(args_dic.keys())[i - 1]] = sys.argv[i]
        i += 1

    # transform args in correct type
    args_dic['iter='] = int(args_dic['iter='])
    args_dic['alpha='] = float(args_dic['alpha='])
    func_dic = {'replace_nan_value': data_parsing.replace_nan_value, 'pandas_remove_nan_line': data_parsing.pandas_remove_nan_line, 'replace_nan_value_by_0': data_parsing.replace_nan_value_by_0}
    args_dic['parse_method='] = func_dic[args_dic['parse_method=']]
    args_dic['batch_size='] = int(args_dic['batch_size='])

    return args_dic


def main():
    ''' Arguments are optionals :
        arg 1 : data in csv file                    (default : 'dataset_train.csv')
        arg 2 : number of iterations                (default : '1000')
        arg 3 : alpha or step for gradient_descent  (default : '0.001')
        arg 4 : parsing method used to filter data  (default : 'replace_nan_value_by_0')
        others choices : ('pandas_remove_nan_line', 'replace_nan_value')
        arg 5 : Bonus Batch_size                    (default : '0' so without bonus)
    '''
    try:
        args = logreg_train_parse_args()
        logreg_train(args['data_csv='], args['parse_method='], args['alpha='], args['iter='], args['batch_size='])
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

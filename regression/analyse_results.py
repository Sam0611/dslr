import pandas as pd
from sklearn.metrics import accuracy_score


def analyse_results(data, predictions):
    """
        Analyse results between original data and the predictions
        Displays number of errors and model's accuracy
    """

    # count errors
    col = "Hogwarts House"
    error = 0
    n = len(predictions)
    for i in range(n):
        if data.loc[i, col] != predictions.loc[i, col]:
            error = error + 1

    # display number of errors and accuracy
    print(f"Number of errors : {error}")
    print(f"Accuracy : {(n - error) / n * 100}%")
    print("sklearn accuracy score :", end=' ')
    print(accuracy_score(data[col], predictions[col]))


def main():
    try:
        data = pd.read_csv("dataset_train.csv")
        predictions = pd.read_csv("houses.csv")
        analyse_results(data, predictions)
    except Exception as error:
        print("Error:", error)


if (__name__ == "__main__"):
    main()

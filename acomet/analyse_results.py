import pandas as pd
from sklearn.metrics import accuracy_score
import sys


def analyse_results(data, predictions, col):
    """
        Analyse results between original data and the predictions
        Displays number of errors and model's accuracy
    """
    accuracy = (data[col] == predictions[col])
    errors = accuracy[accuracy == False].size

    print(f"Number of errors : {errors}")
    print(f"Accuracy : {(accuracy.size - errors) / accuracy.size * 100}%")
    print("sklearn accuracy score :", end=' ')
    print(accuracy_score(data[col], predictions[col]))


def main():
    try:
        dataset_file = "dataset_train.csv"
        predictions_file = "houses.csv"

        argc = len(sys.argv)
        if (argc > 1):
            dataset_file = sys.argv[1]
        if (argc > 2):
            predictions_file = sys.argv[2]

        data = pd.read_csv(dataset_file)
        predictions = pd.read_csv(predictions_file)

        analyse_results(data, predictions, "Hogwarts House")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

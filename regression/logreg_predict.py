import sys
import pandas as pd


def logreg_predict():
    """
        takes dataset_test.csv as a parameter
        and a file containing the weights
        generates a prediction file 'houses.csv'
    """
    if len(sys.argv) != 3:
        raise Exception("Two arguments are required : the path to csv file and file containing the weights")

    # get data from csv file
    data = pd.read_csv(sys.argv[1])


def main():
    try:
        logreg_predict()
    except Exception as error:
        print("Error:", error)


if (__name__ == "__main__"):
    main()

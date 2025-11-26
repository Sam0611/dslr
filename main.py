import pandas as pd

from statistics import get_count, get_mean, get_standard_deviation
from statistics import get_median, get_first_quartile, get_third_quartile
from statistics import get_min, get_max


def load(path: str) -> pd.core.frame.DataFrame:
    """Loads csv file and returns its data"""
    try:
        data = pd.read_csv(path)
        return data
    except Exception:
        return None


def main():
    try:
        data = load("dataset_train.csv")
        col = data["Arithmancy"]
        print("count :", get_count(col))
        print(data.loc[20])
        # print(data.describe())
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

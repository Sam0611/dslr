import pandas as pd
import sys

from statistics import get_count, get_mean, get_standard_deviation
from statistics import get_median, get_first_quartile, get_third_quartile
from statistics import get_min, get_max, get_modes


def load(path: str) -> pd.core.frame.DataFrame:
    """Loads csv file and returns its data"""
    try:
        data = pd.read_csv(path)
        return data
    except Exception:
        return None


def get_not_empty_values(args: any):
    """returns every not empty values"""
    values = []
    for data in args:
        if data == data:
            values.append(data)
    return values


def main():
    try:
        if len(sys.argv) != 2:
            raise Exception("One argument is required : the path to csv file")

        data = load(sys.argv[1])
        numerical_data = data.select_dtypes(include=['number'])

        data_dict = {}
        for name in numerical_data.columns:
            col = get_not_empty_values(data[name])
            if len(col) == 0:
                continue
            data_dict[name] = [
                get_count(col),
                get_mean(col),
                get_standard_deviation(col),
                get_min(col),
                get_first_quartile(col),
                get_median(col),
                get_third_quartile(col),
                get_max(col),
                get_max(col) - get_min(col),
                len(get_modes(col))
            ]

        labels = ["count", "mean", "std", "min", "25%", "50%", "75%", "max", "spread", "number of modes"]
        df = pd.DataFrame(data_dict, index=labels)

        print(data.describe())
        print(df)

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

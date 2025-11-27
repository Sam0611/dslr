
def get_count(args: any):
    """return the number of values"""
    count = 0
    for x in args:
        count += 1
    return count


def get_mean(args: any):
    """return the mean of numbers received"""
    return sum(args) / len(args)


def get_variance(args: any):
    """
        return the variance of numbers received
        (sum((xi - xm)**2) / n)
    """
    mean = get_mean(args)
    numbers = []
    for x in args:
        numbers.append((x - mean) ** 2)
    return sum(numbers) / (len(numbers) - 1)


def get_standard_deviation(args: any):
    """
        return the standard deviation of numbers received
        (square root of variance)
    """
    return get_variance(args) ** 0.5


def get_median(args: any):
    """return the median of numbers received"""
    sorted_args = sorted(args)
    i = int(len(sorted_args) / 2)
    median = sorted_args[i]
    if (len(args) % 2 == 0):
        median = (sorted_args[i] + sorted_args[i - 1]) / 2
    return median


def get_first_quartile(args: any):
    """return the first quartile"""
    median = get_median(args)
    numbers = []
    for x in args:
        if x <= median:
            numbers.append(x)
    return get_median(numbers)


def get_third_quartile(args: any):
    """return the third quartile"""
    median = get_median(args)
    numbers = []
    for x in args:
        if x > median:
            numbers.append(x)
    return get_median(numbers)


def get_min(args: any):
    """return the minimum value"""
    minVal = args[0]
    for x in args:
        if minVal > x:
            minVal = x
    return minVal


def get_max(args: any):
    """return the maximum value"""
    maxVal = args[0]
    for x in args:
        if maxVal < x:
            maxVal = x
    return maxVal

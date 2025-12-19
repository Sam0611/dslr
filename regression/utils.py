import math
import numpy as np


def get_probabilities(num_data, weights):
    """
        Calculates the probability for each row
        p = 1 / (1 + e(-z))
        z = w0 + x1*w1 + xn*wn
    """
    n_rows = len(num_data)
    p = np.array([])
    for i in range(n_rows):
        col = np.array(num_data.loc[i])
        z = 0
        for j in range(len(col)):
            z = z + weights[j] * col[j]
        p = np.append(p, 1 / (1 + math.exp(-z)))
    return p

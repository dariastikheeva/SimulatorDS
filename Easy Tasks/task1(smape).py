'''Numpy module'''

import numpy as np


def smape(y_true: np.array, y_pred: np.array) -> float:
    '''
    Function for calculating sMAPE
    '''
    denominator = np.abs(y_true) + np.abs(y_pred)

    # Replace 0 values with 1s
    denominator = np.where(denominator == 0, 1, denominator)

    return np.mean(2 * np.abs(y_true - y_pred) / denominator)

# print(smape(y_true=np.array([0, 0, 1, 500, 40000]), y_pred=np.array([1, 1, 3, 100, 500])))

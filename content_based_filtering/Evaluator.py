from Recomender import Recommender
import numpy as np


@staticmethod
def mse(model : Recommender, x_data, y_data)-> float:
    mse = np.mean([float((model.predict(x) - y) ** 2) for x, y in zip(x_data,y_data)])
    result = np.sqrt(mse)
    return result


@staticmethod
def rmse(model : Recommender, x_data, y_data)-> float:
    result = np.sqrt(mse(model, x_data, y_data))
    return result


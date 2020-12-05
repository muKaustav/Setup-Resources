import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler as mms
from sklearn.feature_selection import f_regression as freg
from statsmodels.stats.outliers_influence import variance_inflation_factor


def adj_r2(x,y):
    r2 = reg.score(x, y)
    n = x.shape[0]
    p = x.shape[1]

    result = 1 - (1 - r2) * (n - 1) / (n - p - 1)
    return result


def data_summary(x,y):
    r2_score = reg.score(x, y).round(3)
    adj_r2_score = adj_r2(x, y).round(3)
    bias = reg.intercept_.round(5)
    print("R2", end=" ")
    print(r2_score, end="\n")
    print("Adjusted R2", end=" ")
    print(adj_r2_score, end="\n")
    print("Bias", end=" ")
    print(bias, end="\n")


def feature_summary(x,y):
    feature = pd.DataFrame(data = inputs.columns.values, columns=['Features'])
    feature['Weights'] = reg.coef_.round(3)
    feature['P_values'] = freg(x, y)[1].round(3)
    return feature

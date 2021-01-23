from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.feature_selection import f_regression as freg
from sklearn.linear_model import LinearRegression as lr
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import MinMaxScaler as mms
from sklearn.preprocessing import StandardScaler as ss
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# function to show PDFs of non-categorical data


def pdf(a: pd.DataFrame):
    for i in a.columns:
        sns.displot(a[i])

# function to calculate the VIF of features


def vif(a: pd.DataFrame, b: np.array):
    a["VIF"] = [variance_inflation_factor(
        b.values, i) for i in range(b.shape[1])]
    a["Features"] = b.columns
    print(a)

# function to scale inputs using minmaxscaler()


def scaler(a: pd.DataFrame):
    scaler = mms()
    scaler.fit(a)
    return scaler.transform(a)

# function to calculate adujsted R^2 value


def adj_r2(x, y):
    r2 = reg.score(x, y)
    n = x.shape[0]
    p = x.shape[1]
    result = 1 - (1 - r2) * (n - 1) / (n - p - 1)
    return result

# function to summarize the data


def data_summary(x, y):
    r2_score = reg.score(x, y).round(3)
    adj_r2_score = adj_r2(x, y).round(3)
    bias = reg.intercept_.round(5)
    print("R2", end=" ")
    print(r2_score, end="\n")
    print("Adjusted R2", end=" ")
    print(adj_r2_score, end="\n")
    print("Bias/Intercept", end=" ")
    print(bias, end="\n")

# function to summarize the features


def feature_summary(x, y):
    feature = pd.DataFrame(data=inputs.columns.values, columns=['Features'])
    feature['Weights'] = reg.coef_.round(3)
    feature['P_values'] = freg(x, y)[1].round(3)
    return feature

# function to print the prediction table


def predict(a: np.array, b: np.array):
    predictions = pd.DataFrame(np.exp(a), columns=['Predictions'])
    predictions['Target'] = np.exp(b.reset_index(drop=True))
    predictions['Difference%'] = np.absolute(
        ((predictions['Target'] - predictions['Predictions'])/predictions['Target'])*100)
    return predictions

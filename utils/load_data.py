import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split

def load_diabetes():
    diabetes = datasets.load_diabetes()
    diabetes.dropna(inplace=True)
    x, y = diabetes.data, diabetes.target
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.1, random_state=42
    )
    
    return x_train, x_test, y_train, y_test


def load_bank():
    data = pd.read_csv("resources/data/bank-full.csv", sep=";")
    data.dropna(inplace=True)
    x = data.iloc[:,:-1]
    x.drop(columns=["duration", "poutcome"], inplace=True)
    y = data.iloc[:,-1]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.1, random_state=42
    )
    
    return x_train, x_test, y_train, y_test


def load_hillstrom():
    """
    Data about a marketing campaign.
    One possible target variable is whether they came into the store or not.
    """
    data = pd.read_csv("resources/data/Hillstrom.csv", sep=";")
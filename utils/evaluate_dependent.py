import numpy as np
import pandas as pd

import scipy.stats as stats
from statsmodels.stats.anova import AnovaRM

def evaluate_normal_duo(data1, data2):
    test = stats.ttest_rel
    return test(data1, data2)

def evaluate_nonnormal_duo(data1, data2):
    test = stats.wilcoxon
    return test(data1, data2)

def evaluate_normal_group(data):
    rm_anova = AnovaRM(data, "value", "Respondents", within=["variable"])
    results = rm_anova.fit()
    return results.anova_table["Pr > F"]["variable"]

def evaluate_nonnormal_group(data):
    groups = [data.loc[:,i] for i in data.columns]
    test = stats.friedmanchisquare
    return test(*groups)
    
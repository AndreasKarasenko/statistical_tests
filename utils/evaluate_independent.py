import numpy as np
import pandas as pd

import scipy.stats as stats

def evaluate_normal_duo(data1, data2):
    test = stats.ttest_ind
    return test(data1, data2)

def evaluate_nonnormal_duo(data1, data2):
    test = stats.mannwhitneyu()
    return test(data1, data2)

def evaluate_normal_group(data):
    test = stats.f_oneway
    groups = [data.loc[:,i] for i in data.columns]
    return test(*groups)

def evaluate_nonnormal_group(data):
    groups = [data.loc[:,i] for i in data.columns]
    test = stats.kruskal
    return test(*groups)
    
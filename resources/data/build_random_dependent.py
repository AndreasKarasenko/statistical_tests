import pandas as pd
import numpy as np

def normal_dependent2():
    normal1 = np.random.randint(60,80,200)
    normal2 = np.random.randint(50,70,200)
    
    normal = pd.DataFrame(data={
        "Before": normal1,
        "After": normal2}
                          )
    normal.index.name = "Respondents"
                  
    return normal

def nonnormal_dependent2():
    non_normal1 = np.random.rand(7)
    non_nnormal2 = non_normal1 / 1.2
    
    non_normal = pd.DataFrame(data={
        "NewModel": non_normal1,
        "Baseline": non_nnormal2
    })
    non_normal.index.name = "Metrics"
    return non_normal



def normal_dependent_group():
    normal1 = np.random.randint(60,80,200)
    normal2 = np.random.randint(50,70,200)
    normal3 = np.random.randint(55,75,200)
    
    normal = pd.DataFrame(data={
        "Before": normal1,
        "During": normal2,
        "After": normal3}
                          )
    normal.index.name = "Respondents"
                  
    return normal

def nonnormal_dependent_group():
    non_normal1 = np.random.rand(7)
    non_normal2 = non_normal1 / 1.2
    non_normal3 = np.random.rand(7)
    non_normal4 = np.random.rand(7)
    non_normal5 = non_normal1 / 2
    non_normal6 = np.random.rand(7)
    non_normal7 = non_normal1 / 1.1
    
    non_normal = pd.DataFrame(data={
        "NewModel": non_normal1,
        "Baseline1": non_normal2,
        "Baseline2": non_normal3,
        "Baseline3": non_normal4,
        "Baseline4": non_normal5,
        "Baseline5": non_normal6,
        "Baseline6": non_normal7,
    })
    non_normal.index.name = "Metrics"
    return non_normal

import pandas as pd
import numpy as np

def normal_independent2():
    normal1 = np.random.randint(60,80,200)
    normal2 = np.random.randint(50,70,200)
    
    normal = pd.DataFrame(data={
        "Men": normal1,
        "Women": normal2}
                          )
    normal.index.name = "Respondents"
                  
    return normal

def nonnormal_independent2():
    non_normal1 = np.random.rand(7)
    non_nnormal2 = non_normal1 / 1.2
    
    non_normal = pd.DataFrame(data={
        "Men": non_normal1,
        "Women": non_nnormal2
    })
    # non_normal.index.name = "Metrics"
    return non_normal



def normal_independent_group():
    normal1 = np.random.randint(60,80,200)
    normal2 = np.random.randint(50,70,200)
    normal3 = np.random.randint(55,75,200)
    
    normal = pd.DataFrame(data={
        "Cluster1": normal1,
        "Cluster2": normal2,
        "Cluster3": normal3}
                          )
    normal.index.name = "Respondents"
                  
    return normal

def nonnormal_independent_group():
    non_normal1 = np.random.rand(10)
    non_normal2 = non_normal1 / 1.2
    non_normal3 = non_normal1 + 0.2
    
    non_normal = pd.DataFrame(data={
        "Cluster1": non_normal1,
        "Cluster2": non_normal2,
        "Cluster3": non_normal3}
                          )
    non_normal.index.name = "Respondents"
    
    non_normal.index.name = "Metrics"
    return non_normal

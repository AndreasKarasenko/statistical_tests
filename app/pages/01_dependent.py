import streamlit as st
st.set_page_config(layout="wide")

st.title("Dependent")

st.markdown("""
        Samples are considered dependent when the value of one sample depends on another, or
        when they consist of matched pairs. Therefore they are dependent when you can use the members
        of one sample to determine the members of another. 
        Experiments where you repeat one experiment, or use multiple experiments one after another
        lead to dependent samples.
        
        For example: you measure the blood pressure of multiple people, then you give them
        a new drug and meassure the blood pressure again. Each person is paired
        with their previous data point.
        
        In a similar way: if you take a number of algorithms and compare meassure their
        performance across multiple datasets, the datasets are paired as well.
        """)

col1, col2 = st.columns(2)


with col1.expander("Two groups"):
        st.markdown("""
                    For statistical tests of dependent samples with exactly 2 groups
                    we can conduct either a T-test for dependent data, or a signed rank test.
                    
                    The T-test is found as ```scipy.stats.ttest_rel```
                    
                    whereas the signed-rank test is ```scipy.stats.wilcoxon```
                    """)

with col2.expander("More than two groups"):
        st.markdown("""
                    For statistical tests of dependent samples with more than exactly 2 groups
                    we can conduct either a simple repeated meassures ANOVA, or the Friedman test.
                    
                    The T-test is found as ```statsmodels.stats.anova.AnovaRM```
                    
                    whereas the signed-rank test is ```scipy.stats.friedmanchisquare```
                    """)

references = [
        "https://www.geeksforgeeks.org/how-to-perform-a-repeated-measures-anova-in-python/",
        ]
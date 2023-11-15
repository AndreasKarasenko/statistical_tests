import streamlit as st

from resources.data.build_random_dependent import normal_dependent_group
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
                                        """)
        col11, col22 = st.columns(2)
        col11.markdown("The T-test is found as ```scipy.stats.ttest_rel```")
        ttest_button = col11.button("run example", key="ttest_rel")
        
        col22.markdown("The signed-rank test is ```scipy.stats.wilcoxon```")
        wilcoxon_button = col22.button("run example", key="wilcoxon")
        
        dataframe = st.dataframe
        col1_markdown = st.markdown
        
        if ttest_button:
                from resources.data.build_random_dependent import normal_dependent2
                from utils.evaluate_dependent import evaluate_normal_duo
                data = normal_dependent2()
                results = evaluate_normal_duo(data.Before, data.After)
                dataframe(data)
                col1_markdown(f"P-value: {results}")
        if wilcoxon_button:
                from resources.data.build_random_dependent import nonnormal_dependent2
                from utils.evaluate_dependent import evaluate_nonnormal_duo
                data = nonnormal_dependent2()
                results = evaluate_nonnormal_duo(data.NewModel, data.Baseline)
                dataframe(data)
                col1_markdown(f"P-value: {results}")

with col2.expander("More than two groups"):
        col11, col22 = st.columns(2)
        st.markdown("""
                    For statistical tests of dependent samples with more than exactly 2 groups
                    we can conduct either a simple repeated meassures ANOVA, or the Friedman test.
                    
                    """)

        col11, col22 = st.columns(2)
        col11.markdown("The repeated meassures ANOVA is found as ```statsmodels.stats.anova.AnovaRM```")
        anovarm_button = col11.button("run example", key="anovarm")
        
        col22.markdown("The Friedman test is ```scipy.stats.friedmanchisquare```")
        friedman_button = col22.button("run example", key="friedman")
       
        dataframe = st.dataframe
        col2_markdown = st.markdown
        
        if anovarm_button:
                from resources.data.build_random_dependent import normal_dependent2
                from utils.evaluate_dependent import evaluate_normal_group
                data = normal_dependent_group()
                data_long = data.reset_index().melt(id_vars="Respondents")
                results = evaluate_normal_group(data_long)
                dataframe(data)
                col2_markdown(f"P-value: {results}")
        if friedman_button:
                from resources.data.build_random_dependent import nonnormal_dependent_group
                from utils.evaluate_dependent import evaluate_nonnormal_group
                data = nonnormal_dependent_group()
                results = evaluate_nonnormal_group(data)
                dataframe(data)
                col2_markdown(f"P-value: {results}")
                col2_markdown("test")
        
references = [
        "https://www.geeksforgeeks.org/how-to-perform-a-repeated-measures-anova-in-python/",
        ]
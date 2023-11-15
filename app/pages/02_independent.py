import streamlit as st

st.set_page_config(layout="wide")

st.title("Independent")

st.markdown("""
        Independent samples come from a random sampling process where the value
        of 2 or more groups does not influence each other. 
        
        For example: sampling 500 people at random and then seperating them into men and women
        leads to 2 independent groups.
        
        Or: you apply multiple algorithms on datasets where you split the groups according to a demographic
        property (age, sex, etc), these groups are then independent of each other.
        """)


col1, col2 = st.columns(2)


with col1.expander("Two groups"):
        st.markdown("""
                    For statistical tests of independent samples with exactly 2 groups
                    we can conduct either a T-test for independent data, or a Mann-Whitney-U test.
                    
                    The T-test is found as ```scipy.stats.ttest_ind```
                    
                    whereas the Mann-Whitney-U test is ```scipy.stats.mannwhitneyu```
                    """)

with col2.expander("More than two groups"):
        st.markdown("""
                    For statistical tests of dependent samples with more than exactly 2 groups
                    we can conduct a simple one-way ANOVA, or the Kruskal-Wallis test.
                    
                    
                    
                    
                    """)
        col11, col22 = st.columns(2)
        col11.markdown("The one-way ANOVA found as ```scipy.stats.f_oneway```")
        anova_button = col11.button("run example", key="anova")
        
        col22.markdown("The Kruskal-Wallis test is ```scipy.stats.kruskal```")
        kruskal_button = col22.button("run example", key="kruskal")
       
        dataframe = st.dataframe
        col2_markdown = st.markdown
        
        if anova_button:
                from resources.data.build_random_independent import normal_independent_group
                from utils.evaluate_independent import evaluate_normal_group
                data = normal_independent_group()
                results = evaluate_normal_group(data)
                dataframe(data)
                col2_markdown(f"P-value: {results}")
        if kruskal_button:
                from resources.data.build_random_independent import nonnormal_independent_group
                from utils.evaluate_independent import evaluate_nonnormal_group
                data = nonnormal_independent_group()
                results = evaluate_nonnormal_group(data)
                dataframe(data)
                col2_markdown(f"P-value: {results}")
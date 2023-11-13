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
                    
                    The one-way ANOVA found as ```scipy.stats.f_oneway```
                    
                    whereas the Kruskal-Wallis test is ```scipy.stats.kruskal```
                    """)
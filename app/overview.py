import streamlit as st
st.set_page_config(layout="wide")

st.title("Overview")

st.markdown("""
        Statistical tests are generally used to identify significant differences between groups.
        These groups usually are sampled from some population and should be representative of a wider audience.
        However the type of test and when to use it depends on certain properties in the sampled groups.
        
        The most important differentiator is whether the samples are dependent, or independent.
        The second most important is how many groups should be compared. One important difference for tests comparing more than 2 groups
        is: the tests only tell IF there is a significant between ANY group, but not which. For that case you conduct so-called post-hoc tests.
        
        In Python the main way to conduct any statistical test is to use scipy and scikit_posthocs (see the requirements.txt).
        
        We will get 2 values usually, an F-value (or similar) and a p-value.
        The p-value is the probability of observing a test statistic as large or larger than what we observed. We test this value
        against a critical threshold (usually 0.05).
        """)


with st.expander(label="Step by step guide to statistical tests"):
        st.image("./resources/img/step_by_step.png")
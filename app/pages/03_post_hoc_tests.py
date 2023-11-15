import streamlit as st
st.set_page_config(layout="wide")

st.title("Post Hoc Tests")

st.markdown("""
        Post hoc tests are applied after statistical tests that compare 3 or more groups.
        These post hoc tests do pairwise comparisons with (mandatory) corrections for multiple comparisons.
        
        Multiple comparisons add an error term to the p-value so that the chance for a type 1 error (false positive).
        The more often we do a pair-wise comparison the more likely it is that ANY pair will be different by pure chance. 
        """)


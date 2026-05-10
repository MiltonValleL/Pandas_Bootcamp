import streamlit as st

# ---------------------------------------------------------------------
# Sidebar
with st.sidebar:
    st.write("Text in the sidebar")


# ---------------------------------------------------------------------
# Columns
col1, col2, col3 = st.columns(3)

col1.write("Text in a columns")
slider = col2.slider("Choose a number", min_value=0, max_value=10, value=5, step=1)
col3.write(slider)


# ---------------------------------------------------------------------
# Tabs
import pandas as pd

df = pd.read_csv("data/sample.csv")

tab1, tab2 = st.tabs(["Line Plot", "Bar Plot"])

with tab1:
    tab1.write("The following graph is a line plot")
    st.line_chart(df, x="YEAR", y=["COL_1", "COL 2", "COL-3"])

with tab2:
    tab2.write("The following graph is a bar plot")
    st.bar_chart(df, x="YEAR", y=["COL_1", "COL 2", "COL-3"])


# ---------------------------------------------------------------------
# Expander (collapsible element)
with st.expander("Click to expand"):
    st.write("This is a text that you only see when you expand.")


# ---------------------------------------------------------------------
# Container (group elements together)
with st.container():
    st.write("This is inside the container")

st.write("This is outside the container")

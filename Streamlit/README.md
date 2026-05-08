# STREAMLIT PROGRESS *(Spring 1 - Week 1)*

<br><br>

## Thursday, May 07, 2026
1. Today I have installed the Streamlit Python library and Framework.
2. I have learned how to execute **Streamlit** from the terminal.
3. I have learned how to create `Text Elements`.
```Python
import streamlit as st

st.title("Streamlit Progress")

st.header("Text Elements")

st.subheader("How to create a title")

st.markdown("# Header 1")

# Generally used for quotes
st.caption("[Machine learning is the] field of study that gives computers
the ability to learn without being explicitly programmed.")


st.code("""import pandas as pd
df = pd.read_csv(my_csv_file)
df.head()""")


st.text("This is a very basic text")


st.latex("""
\begin{equation}
    y = \beta_0 + \beta_1 x + \epsilon
\end{equation}
""")


# used to creage a division line
st.divider()


st.write("This is a multiple purpose method")
```

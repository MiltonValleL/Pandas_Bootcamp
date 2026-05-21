import numpy as np
import pandas as pd
import streamlit as st

# -----------------------------------------------------------------
# Display almost anything
st.write("Hello Milton. Keep making progress on Streamlit!!!")
st.write("Welcome to streamlit App API")
st.write(1980)

# Display a DataFrame
df = pd.DataFrame(
    {
        "Column 1": [1, 2, 3, 4],
        "Column 2": [10, 20, 30, 40],
        "Column 3": [100, 200, 300, 400],
    }
)
st.write(df)

# Display a Numpy Array
st.write(np.array([1, 2, 3, 4]))
st.divider()

# ------------------------------ MAGIC ------------------------------
st.write("Now it is time to start playing with MAGIC Commands:")

df1 = pd.DataFrame(
    {
        "Name": ["Milton", "Marcela", "Bertha"],
        "Last Name": ["Valle", "Tarraga", "Lora"],
        "Age": [46, 39, 72],
    }
)
df1

# --------------------------------------------------------------
x = 10
x

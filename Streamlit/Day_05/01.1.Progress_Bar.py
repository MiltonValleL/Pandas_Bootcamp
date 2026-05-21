import time

import numpy as np
import streamlit as st

chart_placeholder = st.empty()
# ---------------------------------------------------------
# Plot a line-chart
data = np.random.randn(1, 1)
chart_placeholder = st.line_chart(data)

# ---------------------------------------------------------
# This creates the bar of the left side of the screen
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()


# # Configure the progress number and bar
for i in range(1, 101):
    # np.cumsum() = Sum of all earlier values (cumulative)
    new_data = data + np.random.randn(6, 1).cumsum(axis=0)
    # np.vstack() = Stack arrays vertically, create a single larger array
    data = np.vstack([data, new_data])  # new

    status_text.text(f"{i}% Complete")  # number
    progress_bar.progress(i)  # bar

    chart_placeholder.line_chart(
        data,
        y_label="NVDA - Percentage Change",
        x_label="Time in Minutes",
        color="#83f304",
    )
    time.sleep(0.03)

# ---------------------------------------------------------
progress_bar.empty()
status_text.text("Process Completed!!!")

# Setting a button to re-start
st.button("Regenerate")

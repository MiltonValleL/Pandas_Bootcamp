import time

import numpy as np
import streamlit as st

"""NVDA stock price simulation dashboard."""
# ---------------------------------------------------------
# Constants
INITIAL_POINTS: int = 1
NEW_POINTS_PER_STEP: int = 6
TOTAL_STEPS: int = 100
ANIMATION_DELAY: float = 0.03
CHART_COLOR: str = "#83f304"


# ---------------------------------------------------------
def generate_step(last_value: np.ndarray, n_points: int) -> np.ndarray:
    """Generate next data points using cumulative random walk.

    Args:
        last_value: Last observed value(s) as reference.
        n_points: Number of new points to generate.

    Returns:
        Array of shape (n_points, 1) with simulated values.
    """
    return last_value + np.random.randn(n_points, 1).cumsum(axis=0)


def run_simulation() -> None:
    """Run the stock price simulation dashboard."""
    chart = st.line_chart(np.random.randn(INITIAL_POINTS, 1))
    data = np.random.randn(INITIAL_POINTS, 1)

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    for i in range(1, TOTAL_STEPS + 1):
        new_data = generate_step(data[-1, :], NEW_POINTS_PER_STEP)
        data = np.vstack([data, new_data])

        status_text.text(f"{i}% Complete")
        progress_bar.progress(i)
        chart.line_chart(
            data,
            y_label="NVDA - Percentage Change",
            x_label="Time in Minutes",
            color=CHART_COLOR,
        )
        time.sleep(ANIMATION_DELAY)

    progress_bar.empty()
    status_text.text("Process Completed!!!")
    st.button("Regenerate")


if __name__ == "__main__":
    run_simulation()

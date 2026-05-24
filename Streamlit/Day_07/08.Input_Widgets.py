import datetime
import os

import pandas as pd
import streamlit as st

# ---------------------------------------------------------
st.divider()
st.header("STREAMLIT INPUT WIDGETS")
st.divider()

# ---------------------------------------------------------
# Load Data
df = pd.read_csv("resources/tips.csv")


def display_random_data(df, n: int = 5):
    new_sample = df.sample(n)
    return new_sample


# ---------------------------------------------------------
# BUTTON
# ---------------------------------------------------------
st.subheader("1. Buttons - `st.button()`")
st.markdown("#### Displaying five random rows")
st.caption("Click on the button below to display the row randomly")

button = st.button(
    "Display 5 random rows", type="secondary", icon="💻", icon_position="right"
)
st.write(f"Button = `{button}`")
if button:
    rand_data = display_random_data(df)
    st.dataframe(rand_data)
st.divider()

# ---------------------------------------------------------
# CHECKBOX
# ---------------------------------------------------------
st.subheader("2. Checkbox - `st.checkbox()`")
agree = st.checkbox(label="I agree to terms and conditions")
st.write("Checkbox status = ", agree)

# ---------------------------------------------------------
# MULTIPLE CHECKBOX
# ---------------------------------------------------------
with st.container():
    st.info("What technologies you know?")
    python = st.checkbox("Python")
    ds = st.checkbox("Data Science")
    ml = st.checkbox("Machine Learning")
    ai = st.checkbox("Artifitial Intelligence")
    sklearn = st.checkbox("Scikit-Learng")
    tensor = st.checkbox("Tensor Flow")
    pytorch = st.checkbox("PyTorch")
    tech_button = st.button("Submit")
    if tech_button:
        tech_dict = {
            "Python": python,
            "Data Science": ds,
            "Machine Learning": ml,
            "Artifitial Intelligence": ai,
            "Scikit-Learn": sklearn,
            "Tensor Flow": tensor,
            "PyTorch": pytorch,
        }
        st.json(tech_dict)
st.divider()

# ---------------------------------------------------------
# RADIO BUTTON
# ---------------------------------------------------------
st.subheader("3. Radio Button - `st.radio`")
radio_btn = st.radio(
    label="What is your favorite color?",
    options=("White", "Black", "Blue", "Red", "Green", "Yellow"),
)
st.write("Your favorite color is: ", radio_btn)
st.divider()

# ---------------------------------------------------------
# SELECT BOX
# ---------------------------------------------------------
st.subheader("4. Selectbox - `st.selectbox`")
sel_box = st.selectbox(
    label="What skill you want to learn most?",
    options=("Java", "Python", "C", "C++", "JavaScript", "HTML", "Other"),
)
st.write(f"You selected: {sel_box}")
st.divider()

# ---------------------------------------------------------
# MULTIPLE CHECKBOX
# ---------------------------------------------------------
st.subheader("5. Multi Select Box - `st.multiselect`")
multi = st.multiselect(
    label="What your favorite libraries or Frameworks of ML?",
    options=[
        "Pandas",
        "Numpy",
        "Matplotlib",
        "Seaborn",
        "Plotly",
        "Scikit-Learn",
        "PyTorch",
    ],
)
st.write("You just selected:", multi)
st.divider()

# ---------------------------------------------------------
# SLIDER
# ---------------------------------------------------------
st.subheader("6. Slider - `st.slider()`")
my_slider = st.slider(
    label="What is the loan amount you are looking for?",
    min_value=0,
    max_value=1000,
    value=500,
    step=50,
)
st.write(f"The amount you selected is: `{my_slider}`")
st.divider()

# ---------------------------------------------------------
# TEXT INPUT
# ---------------------------------------------------------
st.subheader("7. Text Input - `st.text_input`")
name = st.text_input(label="Please enter your name: ")
st.write(f"Your name is: `{name}`")
st.divider()

# ---------------------------------------------------------
# NUMBER INPUT
# ---------------------------------------------------------
st.subheader("8. Number Input - `st.number_input`")
numb = st.number_input(
    "Please enter your age: ", min_value=18, max_value=100, step=1, value=30
)
st.write(f"Your age is: `{numb}`")
st.divider()

# ---------------------------------------------------------
# TEXT AREA
# ---------------------------------------------------------
st.subheader("9. Text Area - `st.text_area`")
txt_area = st.text_area(label="Please write you Hobbies:", height=150)
st.divider()

# ---------------------------------------------------------
# DATE INPUT
# ---------------------------------------------------------
start_date = datetime.date(1940, 1, 1)
ref_date = datetime.date(1990, 1, 1)

st.subheader("10. Date Input - `st.date_input`")
date_in = st.date_input(
    label="When is your date of birthday?",
    value=ref_date,
    min_value=start_date,
    max_value="today",
)
st.divider()
# ---------------------------------------------------------
with st.container():
    submit_btn = st.button(label="Submit", key="nano")

    if submit_btn:
        info = {
            "Name": name,
            "Age": numb,
            "Date of Birth": date_in,
            "Description": txt_area,
        }
    else:
        info = {}
    st.json(info)
st.divider()
# ---------------------------------------------------------


# ---------------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------------
st.subheader("11. File Uploader - `st.file_uploader`")

f_upload = st.file_uploader("Choose a file")
save_button = st.button("save file")
if save_button:
    if f_upload is not None:
        with open(os.path.join("resources", f_upload.name), mode="wb") as f:
            f.write(f_upload.getbuffer())
        st.success("The file has been successfully uploaded")
    else:
        st.warning("Please select a file you want to upload")

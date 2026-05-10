import streamlit as st

# # ------------------------------------------------------
st.title("Claude Bootcamp - Day 3")
st.subheader("Saturday, May 09, 2026")


# ----------------------------------------------------------------------------------
with st.form("form_key"):
    st.markdown("### What would you like to order?")

    appetizers = st.selectbox(
        label="Appetizers", options=["Choise 1", "Choise 2", "Choise 3"], index=0
    )
    main = st.selectbox(
        label="Main Course", options=["Choise 1", "Choise 2", "Choise 3"], index=1
    )
    dessert = st.selectbox(
        label="Dessert", options=["Choise 1", "Choise 2", "Choise 3"], index=2
    )

    wine = st.checkbox(label="Are you bringing your own wine?")

    visit_date = st.date_input(label="When are you coming?")
    visit_time = st.time_input(label="At what time are you coming?")

    allergies = st.text_area(
        label="Any allergies?", height=180, placeholder="Leave us a note for allergies"
    )

    submit_btn = st.form_submit_button(label="Submit")
# ----------------------------------------------------------------------------------
st.write(f"""Your order summary:

         - Appetizer: {appetizers:>31}
         - Main Course: {main:>29}
         - Dessert: {dessert:>33}
         - Are you bringing your own wine:\t{"Yes" if wine else "No"}
         - Date of visit:\t\t\t{visit_date}
         - Time of visit:\t\t\t{visit_time}
         - Allergies:\t\t\t\t{allergies}
         """)
# ----------------------------------------------------------------------------------

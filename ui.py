import streamlit as st
from db import *

st.title("🏏 Cricket Players Details")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Insert", "Update", "Display", "Delete"]
)

# ---------------- INSERT ----------------

if menu == "Insert":

    st.header("Insert Record")

    name = st.text_input("Player Name")
    t20score = st.number_input("T20 Score", step=1)
    testscore = st.number_input("Test Score", step=1)
    odiscore = st.number_input("ODI Score", step=1)
    toprank = st.number_input("Top Rank", step=1)

    if st.button("Save", key="save"):
        st.success("""
            insert_record(
                name,
                t20score,
                testscore,
                odiscore,
                toprank
            )
       """ )

# ---------------- UPDATE ----------------

elif menu == "Update":

    st.header("Update Record")

    player_id = st.number_input("Enter ID", min_value=1, step=1)

    if st.button("Search", key="search"):

        data = retrieve_record(player_id)

        if data:
            st.session_state["id"] = data[0]
            st.session_state["name"] = data[1]
            st.session_state["t20score"] = data[2]
            st.session_state["testscore"] = data[3]
            st.session_state["odiscore"] = data[4]
            st.session_state["toprank"] = data[5]

        else:
            st.error("Record Not Found")

    if "id" in st.session_state:

        name = st.text_input(
            "Player Name",
            value=st.session_state["name"]
        )

        t20score = st.number_input(
            "T20 Score",
            value=int(st.session_state["t20score"])
        )

        testscore = st.number_input(
            "Test Score",
            value=int(st.session_state["testscore"])
        )

        odiscore = st.number_input(
            "ODI Score",
            value=int(st.session_state["odiscore"])
        )

        toprank = st.number_input(
            "Top Rank",
            value=int(st.session_state["toprank"])
        )

        if st.button("Update", key="update"):

            st.success(
                update_record(
                    st.session_state["id"],
                    name,
                    t20score,
                    testscore,
                    odiscore,
                    toprank
                )
            )

# ---------------- DISPLAY ----------------

elif menu == "Display":

    st.header("All Players")

    records = display_records()

    if records:
        st.table(records)
    else:
        st.info("No Records Found")

# ---------------- DELETE ----------------

elif menu == "Delete":

    st.header("Delete Record")

    player_id = st.number_input(
        "Enter ID",
        min_value=1,
        step=1
    )

    if st.button("Delete", key="delete"):
        st.success(delete_record(player_id))

















    

    
























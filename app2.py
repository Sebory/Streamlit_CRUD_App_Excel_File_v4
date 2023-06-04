import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config("Data Entry Form", layout="wide", page_icon=":newspaper:")

df = pd.read_excel("data/Fruits.xlsx", engine="openpyxl", index_col=0)
# --------------- SIDE BAR ----------------
side_bar = st.sidebar.radio("Please Select Here:", ["Data Entry Form", "Data Update Form", "Data Filter/Update"])

if side_bar == "Data Entry Form":
    # --------- DATA ENTRY FORM -------------------
    st.title("Data Entry Form")

    dt_entry_frm = st.form("data_entry", clear_on_submit=True)
    fruits = dt_entry_frm.text_input("Fruits")
    quantite = dt_entry_frm.text_input("Quantité")
    pu = dt_entry_frm.text_input("PU")
    # pt = dt_entry_frm.text_input("PT")
    submit_bt = dt_entry_frm.form_submit_button("Submit")

    if submit_bt:
        new_data = pd.DataFrame({"Fruits":[fruits], "Quantité":[int(quantite)], "PU":[int(pu)]})
        new_data["PT"] = new_data["Quantité"]*new_data["PU"]
        data_updated = df.append(new_data, ignore_index=True)
        data_updated.to_excel("data/Fruits.xlsx", index=False)

        st.success("Submited")



    df2 = pd.read_excel("data/Fruits.xlsx", engine="openpyxl", index_col=0)

    if st.checkbox("Show Data"):
        st.dataframe(df2, use_container_width=True)

if side_bar == "Data Update Form":
    st.title("Data Update Table")
    df2 = pd.read_excel("data/Fruits.xlsx", engine="openpyxl", index_col=0)
    x = st.data_editor(df2, num_rows="dynamic", use_container_width=True)

    if st.button("Submit"):
        x.to_excel("data/Fruits.xlsx", index=True)

if side_bar == "Data Filter/Update":
    st.title("Data Filter/Update")
    df2 = pd.read_excel("data/Fruits.xlsx", engine="openpyxl", index_col=0)
    fruit = st.multiselect("Please select Fruits for filtering:", df["Fruits"].unique().tolist())
    df_selection = df2.query("Fruits == @fruit")
    y = st.data_editor(df_selection, num_rows="dynamic", use_container_width=True) 
    st.markdown("---")

    if st.button("Update"):
        y.to_excel("data/fruits_for_update.xlsx", index=True)
        df_fruits_for_updt = pd.read_excel("data/fruits_for_update.xlsx", engine="openpyxl", index_col=0)
        df2.loc[df_fruits_for_updt.index] = df_fruits_for_updt
        df2.to_excel("data/Fruits.xlsx", index=True)
    






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
        # data_updated = df.append(new_data, ignore_index=True)
        data_updated = pd.concat([df, new_data], ignore_index=True)
        data_updated.to_excel("data/Fruits.xlsx", index=True)

        st.success("Submited")



    df2 = pd.read_excel("data/Fruits.xlsx", engine="openpyxl", index_col=0)

    if st.checkbox("Show Data"):
        st.dataframe(df2, use_container_width=True)

if side_bar == "Data Update Form":
    st.title("Data Update Table")
    df2 = pd.read_excel("data/Fruits.xlsx", engine="openpyxl", index_col=0)
    x = st.experimental_data_editor(df2, num_rows="dynamic", use_container_width=True)

    if st.button("Submit"):
        x.to_excel("data/Fruits.xlsx", index=True)

if side_bar == "Data Filter/Update":
    st.title("Data Filter/Update")
    df2 = pd.read_excel("data/Fruits.xlsx", engine="openpyxl", index_col=0)
    fruit = st.multiselect("Please select Fruits for filtering:", df["Fruits"].unique().tolist())
    df_selection = df2.query("Fruits == @fruit")
    y = st.experimental_data_editor(df_selection, num_rows="dynamic", use_container_width=True) 
    st.markdown("---")

    if st.button("Update"):
        y.to_excel("data/fruits_for_update.xlsx", index=True)
        df_fruits_for_updt = pd.read_excel("data/fruits_for_update.xlsx", engine="openpyxl", index_col=0)
        df2.loc[df_fruits_for_updt.index] = df_fruits_for_updt
        df2.to_excel("data/Fruits.xlsx", index=True)
    
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ----------- LET MAKE PAGE FOOTER --------------
import streamlit as st

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by Dr Diaby A. S.</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)





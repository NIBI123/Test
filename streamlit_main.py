import streamlit as st
st.set_page_config(layout="wide")

def intro():
    st.write("# Testng testing testing! 👋")

page_names_to_funcs = {
    "Hovedside": intro,
}

demo_name = st.sidebar.selectbox("Vælg en side", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

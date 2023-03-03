import streamlit as st
import pathlib
from bs4 import BeautifulSoup
import logging
import shutil
import pandas as pd
st.set_page_config(layout="wide")

def intro():
    st.write("# Velkommen til bottenAnna's Fantasy Site! 👋")

page_names_to_funcs = {
    "Hovedside": intro,
}

demo_name = st.sidebar.selectbox("Vælg en side", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

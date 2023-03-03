import streamlit as st
from holdetDK_WebApp import playersValCalc, distanceToTopCalc, teamValTopCalc, modelBeskrivelseCalc, optakterCalc, \
    popularitsprocenterCalc, predictedLineupsCalc, GWinfoCalc, runderCalc, highscoreCalc, forsideCalc, lineupDataCalc
import pathlib
from bs4 import BeautifulSoup
import logging
import shutil
import pandas as pd
st.set_page_config(layout="wide")

def intro():
    forsideCalc()

def optakter():
    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    optakterCalc()

def playerVal():
    st.markdown(f'# {list(page_names_to_funcs.keys())[2]}')
    playersValCalc()

def predictedLineups():
    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    predictedLineupsCalc()

def teamVal():
    st.markdown(f"# {list(page_names_to_funcs.keys())[4]}")
    teamValTopCalc()

def popularitsprocenter():
    st.markdown(f'# {list(page_names_to_funcs.keys())[5]}')
    popularitsprocenterCalc()

def highscore():
    st.markdown(f'# {list(page_names_to_funcs.keys())[6]}')
    highscoreCalc()

def distanceToTop():
    st.markdown(f"# {list(page_names_to_funcs.keys())[7]}")
    distanceToTopCalc()

def modelBeskrivelse():
    st.markdown(f'# {list(page_names_to_funcs.keys())[8]}')
    modelBeskrivelseCalc()

def GWinfo():
    st.markdown(f'# {list(page_names_to_funcs.keys())[9]}')
    GWinfoCalc()

def runder():
    st.markdown(f'# {list(page_names_to_funcs.keys())[10]}')
    runderCalc()

def lineupData():
    st.markdown(f'# {list(page_names_to_funcs.keys())[11]}')
    lineupDataCalc()

page_names_to_funcs = {
    "Hovedside": intro,
    "Optakter": optakter,
    "Player value": playerVal,
    "Predicted Lineups": predictedLineups,
    "Team value": teamVal,
    "Popularitetsprocenter": popularitsprocenter,
    "Præmiepulje tabel": highscore,
    "Point distance to rank": distanceToTop,
    "Model beskrivelse": modelBeskrivelse,
    "gameweek info": GWinfo,
    "Runder": runder,
    "Scraped lineups": lineupData

}

demo_name = st.sidebar.selectbox("Vælg en side", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

def inject_ga():
    GA_ID = "google_analytics"


    GA_JS = """
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-V1N5YGSC0Q"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-V1N5YGSC0Q');
    </script>
    """

    # Insert the script in the head tag of the static template inside your virtual
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    logging.info(f'editing {index_path}')
    soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    if not soup.find(id=GA_ID):
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)
        else:
            shutil.copy(index_path, bck_index)
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + GA_JS)
        index_path.write_text(new_html)

inject_ga()
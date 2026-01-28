# app.py

import streamlit as st

#importation des textes
import contenu 

#importation des sources
from contenu import liste_sources

# Configuration
st.set_page_config(page_title="Concorde NSI", layout="wide")

# Navigation
slides = ["1. Intro", "2. Ailes"]
choix = st.sidebar.radio("Sommaire", slides)

# --- SLIDE 1 ---
if choix == "1. Intro":
    st.image("images/Presentation_1.png")

# --- SLIDE 2 ---
elif choix == "2. Ailes":
    st.title(contenu.titre_ailes)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/Gothic Delta Wings.jpeg")
    with col2:
        st.markdown(contenu.details_ailes)

# --- SLIDE sources ---

st.title("Sources & Bibliographie")

for s in contenu.liste_sources:
    st.write(f"📖 {s}")
# app.py

import streamlit as st
import contenu  # <--- C'est ici que la magie opère !

# Configuration
st.set_page_config(page_title="Concorde NSI", layout="wide")

# Navigation
slides = ["1. Intro", "2. Ailes"]
choix = st.sidebar.radio("Sommaire", slides)

# --- SLIDE 1 ---
if choix == "1. Intro":
    st.title(contenu.titre_intro)  # On va chercher le titre dans l'autre fichier
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(contenu.texte_contexte)
    with col2:
        st.image("images/concorde_vol.jpg")

# --- SLIDE 2 ---
elif choix == "2. Ailes":
    st.title(contenu.titre_ailes)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/aile_delta.jpg")
    with col2:
        st.markdown(contenu.details_ailes)
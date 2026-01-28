# app.py

import streamlit as st

#importation des textes
import contenu 

from contenu import *
#importation des sources
from contenu import liste_sources

# Configuration
st.set_page_config(page_title="Concorde story", layout="wide")

# --- MENU LATÉRAL ---
st.sidebar.title("Sommaire")
pages = [
    "Home", 
    "The Beginning", 
    "The Supersonic Race", 
    "Key Numbers", 
    "Performance", 
    "The Wings", 
    "The Engines", 
    "Fly by Wire", 
    "The Nose", 
    "Fuel Management",
    "The End of Concorde",  # NOUVEAU
    "The Future",           # NOUVEAU
    "Vocabulary"
]
selection = st.sidebar.radio("Go to:", pages)

# --- PAGES ---

if selection == "Home":
    st.title(titre_principal)
    st.write(f"**{auteur}**")
    st.image("concorde_home.jpg", use_container_width=True) # Slide 1

elif selection == "The Beginning":
    st.header(titre_debut)
    col1, col2 = st.columns(2)
    with col1:
        st.write(texte_debut)
    with col2:
        st.image("logos_slide2.jpg") # Slide 2

elif selection == "The Supersonic Race":
    st.header(titre_course)
    st.write(texte_course)
    col1, col2 = st.columns(2)
    with col1:
        st.image("tu144.jpg", caption="Tupolev Tu-144")
    with col2:
        st.image("boeing2707.jpg", caption="Boeing 2707")

elif selection == "Key Numbers":
    st.header(titre_chiffres)
    st.info(texte_chiffres)
    st.image("first_flight.jpg", caption="First flight 1969")

elif selection == "Performance":
    st.header(titre_perf)
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🚀 Concorde")
        st.metric("Speed", stats_concorde["Speed"])
        st.metric("Altitude", stats_concorde["Altitude"])
    with c2:
        st.subheader("✈️ Normal Plane")
        st.metric("Speed", stats_normal["Speed"])
        st.metric("Altitude", stats_normal["Altitude"])

elif selection == "The Wings":
    st.header(titre_ailes)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.write(texte_ailes)
    with c2:
        st.image("delta_wing.jpg")

elif selection == "The Engines":
    st.header(titre_moteurs)
    st.write(texte_moteurs)
    st.image("engine.jpg")

elif selection == "Fly by Wire":
    st.header(titre_fbw)
    c1, c2 = st.columns(2)
    with c1:
        st.write(texte_fbw)
    with c2:
        st.image("fadec.jpg")

elif selection == "The Nose":
    st.header(titre_nez)
    tab1, tab2 = st.tabs(["Landing", "Cruise"])
    with tab1:
        st.write(texte_nez_baisse)
        st.image("nose_down.jpg")
    with tab2:
        st.write(texte_nez_haut)
        st.image("nose_up.jpg")

elif selection == "Fuel Management":
    st.header(titre_fuel)
    st.warning(texte_fuel)
    st.image("fuel_system.jpg")

# --- NOUVELLE PAGE : THE END ---
elif selection == "The End of Concorde":
    st.header(titre_fin)
    st.subheader(f"😢 {sous_titre_fin}")
    
    col1, col2 = st.columns(2)
    with col1:
        for cause in causes_fin:
            st.error(cause) # st.error met le texte en rouge
            
    with col2:
        # Pense à mettre une image du crash ou du dernier vol ici
        st.image("concorde_end.jpg", caption="The final flight")

# --- NOUVELLE PAGE : FUTURE ---
elif selection == "The Future":
    st.header(titre_futur)
    st.success(texte_futur) # st.success met le texte en vert
    # Tu peux mettre une image d'un projet futur (ex: Overture de Boom Supersonic)
    st.image("future_supersonic.jpg", caption="The next generation?")

elif selection == "Vocabulary":
    st.header(titre_vocab)
    for mot, def in vocabulaire.items():
        st.markdown(f"**{mot}** : {def}")
st.title("Sources & Bibliographie")

for s in contenu.liste_sources:
    st.write(f"📖 {s}")
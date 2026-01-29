# app.py

import streamlit as st

#importation des textes
import contenu 

from contenu import *
#importation des sources
from contenu import liste_sources

#controle des fleches pour passer les diapos
import streamlit.components.v1 as components
# Configuration
st.set_page_config(page_title="Concorde story by Antoine", layout="wide")

# --- Taille des textes ---
st.markdown("""
<style>
    html, body, p, li, .stMarkdown {
        font-size: 24px !important;
    }
    h1 { font-size: 60px !important; }
    h2 { font-size: 45px !important; }
    h3 { font-size: 35px !important; }
    .stAlert { font-size: 24px !important; }
    .stImageCaption { font-size: 18px !important; }
</style>
""", unsafe_allow_html=True)

#controle des fleches pour passer les diapos
def navigation_clavier():
    components.html("""
    <script>
    const doc = window.parent.document;
    doc.addEventListener('keydown', function(e) {
        // Si Flèche Droite -> On cherche le bouton "Next"
        if (e.key === 'ArrowRight') {
            const buttons = doc.querySelectorAll('button');
            buttons.forEach(btn => {
                if (btn.innerText.includes('Next ➡️')) {
                    btn.click();
                }
            });
        }
        // Si Flèche Gauche -> On cherche le bouton "Prev"
        if (e.key === 'ArrowLeft') {
            const buttons = doc.querySelectorAll('button');
            buttons.forEach(btn => {
                if (btn.innerText.includes('⬅️ Prev')) {
                    btn.click();
                }
            });
        }
    });
    </script>
    """, height=0, width=0)


# --- MENU LATÉRAL & NAVIGATION ---
st.sidebar.title("Summary")

# 1. On définit la liste des pages
pages = [
    "Home", 
    "The Beginning", 
    "The Supersonic Race", 
    "Key Numbers", 
    "Performance", 
    "The Gothic Delta Wings", 
    "The Engines", 
    "Fly by Wire", 
    "The Droop Nose", 
    "Fuel Management",
    "The End of Concorde",
    "The Future",
    "Vocabulary"
]

# 2. On initialise la page actuelle dans la mémoire si elle n'existe pas
if "page_actuelle" not in st.session_state:
    st.session_state.page_actuelle = pages[0]

# 3. Fonction pour changer de page (Précédent / Suivant)
def changer_page(delta):
    # On cherche où on est dans la liste (ex: index 0, 1, 2...)
    index_actuel = pages.index(st.session_state.page_actuelle)
    # On calcule le nouvel index (le % len(pages) permet de boucler à la fin)
    nouveau_index = (index_actuel + delta) % len(pages)
    # On met à jour la mémoire
    st.session_state.page_actuelle = pages[nouveau_index]

# 4. On affiche les boutons de navigation en haut du menu
col_prev, col_next = st.sidebar.columns(2)

if col_prev.button("⬅️ Prev"):
    changer_page(-1)
    st.rerun() # Force le rechargement immédiat

if col_next.button("Next ➡️"):
    changer_page(1)
    st.rerun()

# 5. Le Menu Radio (connecté à la mémoire via la clé 'page_actuelle')
selection = st.sidebar.radio(
    "Go to:", 
    pages, 
    key="page_actuelle" # C'est ici que la magie opère : le bouton radio suit la mémoire
)
# --- PAGES ---

if selection == "Home":
    st.image("images/Presentation_1.png", use_container_width=True) # Slide 1

elif selection == "The Beginning":
    st.header(titre_debut)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(texte_debut)
        st.image("images/Sud-Aviation-1961-P1.jpeg")
    with col2:
        st.image("images/british-aircraft-corporation.png") # Slide 2
    with col3:
        st.image("images/concorde_treaty.jpg")

elif selection == "The Supersonic Race":
    st.header(titre_course)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(texte_course)
        st.image("images/Tupolev Tu-144.jpg", caption="Tupolev Tu-144")    
    with col2:
        st.image("images/boeing-2707.jpg", caption="Boeing 2707")
        st.image("images/Boeing 2707.jpeg", caption="Boeing 2707")
    with col3:
        st.image("images/Tupolev Tu-144.webp", caption="Tupolev Tu-144")
        
        

elif selection == "Key Numbers":
    st.header(titre_chiffres)
    st.info(texte_chiffres)
    st.image("images/5concordes.gif")

elif selection == "Performance":
    st.header(titre_perf)
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Concorde")
        st.metric("Speed", stats_concorde["Speed"])
        st.metric("Altitude", stats_concorde["Altitude"])
        # AJOUT DE use_container_width=True
        st.image("images/ConcordeAileface.png", caption="Concorde", use_container_width=True)
        
    with c2:
        st.subheader("Normal Plane")
        st.metric("Speed", stats_normal["Speed"])
        st.metric("Altitude", stats_normal["Altitude"])
        # AJOUT DE use_container_width=True
        st.image("images/comet.png", caption="De Havilland Comet DH-106", use_container_width=True)


elif selection == "The Gothic Delta Wings":
    st.header(titre_ailes)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c1:
        st.write(texte_ailes)
    with c2:
        st.image("images/Gothic Delta Wings3.jpg")
    with c3:
        st.image("images/Gothic Delta Wings2.jpeg")
        st.image("images/Gothic Delta Wings4.jpeg")

elif selection == "The Engines":
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header(titre_moteurs)
        st.write(texte_moteurs)
    with col2:
        st.image("images/intakes.png")
    with col3:
        st.image("images/Olympus 593 Engines_intakes.avif")
        st.image("images/Rolls-Royce-Snecma_Olympus_-_Musée_Safran.jpg")
        

elif selection == "Fly by Wire":
    
    # Tu peux changer [1, 1] par [1, 1.5] si tu veux que l'image soit encore plus large que le texte
    c1, c2 = st.columns([1, 1.2]) 
    
    with c1:
        # Les "###" devant la variable transforment le texte en "Titre 3" (plus gros)
        st.header(titre_fbw)
        st.markdown(f"### {texte_fbw}")
        
    with c2:
        # use_container_width=True oblige l'image à s'étirer au maximum
        st.image("images/FADEC.jpg", use_container_width=True)

# --- SLIDE 9 : THE droop NOSE ---
elif selection == "The Droop Nose": # (ou "The Nose" selon ton menu)
    st.header(titre_nez)
    
    # 1. Les textes explicatifs dans les onglets
    tab1, tab2 = st.tabs(["Landing/Take-off", "Supersonic Cruise"])
    
    with tab1:
        st.write(texte_nez_baisse)
        
    with tab2:
        st.write(texte_nez_haut)

    # 2. La vidéo de démonstration (en dessous pour être toujours visible)
    st.write("---") # Une ligne de séparation
    st.subheader("Mechanism Demonstration")
    # Assure-toi que le nom du fichier est EXACTEMENT le même (majuscules/espaces)
    st.video("images/Concorde droop nose and visor test.mp4")

elif selection == "Fuel Management":
    st.header(titre_fuel)
    
    c1, c2 = st.columns([1, 1.2]) 
    
    with c1:
        # Les "###" devant la variable transforment le texte en "Titre 3" (plus gros)
        st.markdown(f"### {texte_fuel}")
        st.image("images/Fuel.png")
    with c2:
        # use_container_width=True oblige l'image à s'étirer au maximum
        st.image("images/Fuel2.png",use_container_width=True)

# --- NOUVELLE PAGE : THE END ---
# --- NOUVELLE PAGE : THE END ---
elif selection == "The End of Concorde":
    st.header(titre_fin)
    st.subheader(f"😢 {sous_titre_fin}")
    
    # On fait des colonnes inégales : le texte à gauche (40%), les images à droite (60%)
    col1, col2 = st.columns([1, 1.5]) 
    
    with col1:
        # AMÉLIORATION TEXTE : Un seul bloc rouge contenant une liste propre
        st.error("### Main Causes:") # Un petit titre dans la boîte rouge
        text_causes = ""
        for cause in causes_fin:
            text_causes += f"- {cause}\n" # On construit une liste Markdown
        st.markdown(text_causes)
            
    with col2:
        # AMÉLIORATION IMAGES : Disposition en mosaïque
        # 1. La grande image principale (Le décollage en feu)
        st.image("images/crash3.jpg", caption="Crash in Gonesse - July 2000", use_container_width=True)
        
        # 2. Les deux autres images côte à côte juste en dessous
        sub_c1, sub_c2 = st.columns(2)
        with sub_c1:
            st.image("images/crash2.jpeg", use_container_width=True)
        with sub_c2:
            st.image("images/crash.jpeg", use_container_width=True)

# --- NOUVELLE PAGE : FUTURE ---
elif selection == "The Future":
    st.header(titre_futur)
    
    # Zone de texte en haut
    st.info(texte_futur) 

    # Création de deux colonnes inégales (La gauche est plus large)
    col1, col2 = st.columns([1.5, 1])

    with col1:
        # Grande image : L'avion en vol (Design concept)
        st.image("images/Lockheed-Martin-Quesst-X-59.jpeg", caption="The X-59 QueSST Concept", use_container_width=True)

    with col2:
        # Petite colonne de droite : Le Logo puis le test moteur
        c1, c2 = st.columns([1, 2]) # On centre un peu le logo
        with c2:
            st.image("images/NASA.png", width=120) # Logo NASA un peu réduit
            
        st.write("") # Juste un petit espace vide
        st.image("images/Nasa_X59.jpg", caption="Tail Engine Test", use_container_width=True)

elif selection == "Vocabulary":
    st.header(titre_vocab)
    st.write("") # Un peu d'espace
    
    # On crée 2 colonnes
    col1, col2 = st.columns(2)
    
    # On transforme le dictionnaire en liste pour pouvoir compter (0, 1, 2, 3...)
    items = list(vocabulaire.items())
    
    for index, (mot, definition) in enumerate(items):
        # Si le numéro est PAIR (0, 2, 4...), on met dans la colonne de GAUCHE
        if index % 2 == 0:
            with col1:
                st.markdown(f"## **{mot}** : {definition}")
                st.markdown("---") # Ligne de séparation
        
        # Si le numéro est IMPAIR (1, 3, 5...), on met dans la colonne de DROITE
        else:
            with col2:
                st.markdown(f"## **{mot}** : {definition}")
                st.markdown("---")

navigation_clavier()
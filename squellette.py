import streamlit as st

# 1. SETUP (Tout l'écran)
st.set_page_config(page_title="Ma Présentation", layout="wide")

# 2. NAVIGATION (Menu à gauche)
# Liste tes parties ici
slides = ["Introduction", "Partie Principale", "Conclusion"]
current_slide = st.sidebar.radio("Aller à :", slides)

# 3. CONTENU (Logique des pages)

# --- PAGE 1 ---
if current_slide == "Introduction":
    st.title("Bienvenue sur mon Projet")
    st.write("Ceci est l'introduction.")

# --- PAGE 2 ---
elif current_slide == "Partie Principale":
    st.title("Le cœur du sujet")
    
    # Création de 2 colonnes
    col_texte, col_image = st.columns([2, 1]) # Texte 2x plus large que l'image
    
    with col_texte:
        st.write("Ici je mets mes explications détaillées.")
        st.info("Note importante : Le Concorde allait très vite.")
        
    with col_image:
        st.write("Ici je mettrai une image")
        # st.image("dossier/image.jpg")

# --- PAGE 3 ---
elif current_slide == "Conclusion":
    st.title("Merci de votre écoute")
    st.balloons() # Petite animation fun de fin
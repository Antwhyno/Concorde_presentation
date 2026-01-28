# The Concorde

### Apprentissage des bases streamlit:

st : C'est le petit nom (l'alias) que tu as donné à Streamlit au début de ton fichier (import streamlit as st). Ça dit à Python : "Hé, utilise l'outil Streamlit".

.title : C'est la fonction spécifique qui dit "Je veux afficher un titre géant".

("Sources & Bibliographie") : C'est l'argument. C'est le texte exact qui va apparaître sur ton écran.

### La hiérarchie des titres dans Streamlit
st.title()	🏆 Géant	Titre de la diapositive (ex: Le Concorde)
st.header()	🥈 Grand	Titre d'une section (ex: Caractéristiques techniques)
st.subheader()	🥉 Moyen	Sous-titre (ex: Les moteurs Olympus)
st.write()	📝 Normal	Ton texte de paragraphe, tes explications.

### Les colonnes, with dans streamlit
En Python, le with s'appelle un "Context Manager" (Gestionnaire de contexte), le with sert de "conteneur visuel"

1. L'analogie de la boîte
Imagine que chaque colonne que tu crées est une boîte vide.

Si tu écris st.image() tout seul, Streamlit pose l'image par terre, au milieu de la page.

Si tu utilises with col1:, tu dis à Python : "Ouvre la boîte col1, et tout ce que je vais écrire (tant que c'est décalé vers la droite) doit être rangé à l'intérieur de cette boîte."

Dès que tu arrêtes de décaler ton code (l'indentation), la boîte se referme.

Exemple:
col1, col2 = st.columns(2)

with col1:
    st.write("Ceci est bien DANS la colonne de gauche.")
    st.image("avion.jpg") # Aussi dans la colonne de gauche

with col2:
    st.write("Ceci est bien DANS la colonne de droite.")

### Les sections expansibles

C'est une section qui cache du texte ou des images par défaut. L'utilisateur doit cliquer sur une petite flèche pour "déplier" le contenu.

Exemple:
with st.expander("Clique ici pour voir les détails secrets"):
    st.write("Voici les informations confidentielles...")
    st.image("photo_top_secret.jpg")


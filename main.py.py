import streamlit as st
import io

st.set_page_config(page_title="README Generator", page_icon="📝", layout="centered")

st.title("📝 README Generator")
st.write("Générez un fichier `README.md` propre et professionnel pour vos projets en quelques secondes.")

st.divider()

# Formulaire de génération
with st.form("readme_form"):
    st.subheader("Informations du projet")
    
    col1, col2 = st.columns(2)
    with col1:
        nom = st.text_input("Nom du projet *", placeholder="Mon Super Projet")
        auteur = st.text_input("Votre nom / pseudo GitHub *", placeholder="camatcho5")
    with col2:
        description = st.text_input("Description courte *", placeholder="Un outil qui fait des choses géniales.")
        technologies = st.text_input("Technologies (séparées par des virgules)", placeholder="Python, Streamlit, Pillow")
    
    installation = st.text_input("Commande d'installation", value="pip install -r requirements.txt")
    usage = st.text_input("Commande d'utilisation", value="streamlit run app.py")
    
    # Bouton de soumission
    submitted = st.form_submit_button("Générer le README", type="primary", use_container_width=True)

if submitted:
    if not nom or not auteur or not description:
        st.error("⚠️ Veuillez remplir les champs obligatoires (marqués d'une étoile).")
    else:
        # Construction du contenu Markdown
        contenu = f"""# {nom}

{description}

## 🚀 Technologies

- {technologies}

## 📦 Installation

```bash
{installation}

import streamlit as st

st.set_page_config(page_title="README Generator", page_icon="📝", layout="centered")

st.title("📝 README Generator")
st.write("Générez un fichier README.md propre et professionnel pour vos projets en quelques secondes.")

st.divider()

with st.form("readme_form"):
    st.subheader("Informations du projet")
    
    col1, col2 = st.columns(2)
    with col1:
        nom = st.text_input("Nom du projet *", placeholder="Mon Super Projet")
        auteur = st.text_input("Votre nom / pseudo GitHub *", placeholder="camatcho5")
    with col2:
        description = st.text_input("Description courte *", placeholder="Un outil qui fait des choses géniales.")
        technologies = st.text_input("Technologies (séparées par des virgules)", placeholder="Python, Streamlit")
    
    installation = st.text_input("Commande d'installation", value="pip install -r requirements.txt")
    usage = st.text_input("Commande d'utilisation", value="streamlit run app.py")
    
    submitted = st.form_submit_button("Générer le README", type="primary", use_container_width=True)

if submitted:
    if not nom or not auteur or not description:
        st.error("⚠️ Veuillez remplir les champs obligatoires (marqués d'une étoile).")
    else:
        # Construction du texte ligne par ligne pour éviter les erreurs de guillemets
        lignes = []
        lignes.append("# " + nom)
        lignes.append("")
        lignes.append(description)
        lignes.append("")
        lignes.append("## 🚀 Technologies")
        lignes.append("")
        lignes.append("- " + technologies)
        lignes.append("")
        lignes.append("## 📦 Installation")
        lignes.append("")
        lignes.append("```bash")
        lignes.append(installation)
        lignes.append("```")
        lignes.append("")
        lignes.append("## 💻 Utilisation")
        lignes.append("")
        lignes.append("```bash")
        lignes.append(usage)
        lignes.append("```")
        lignes.append("")
        lignes.append("## 👤 Auteur")
        lignes.append("")
        lignes.append("- **" + auteur + "** — [GitHub](https://github.com/" + auteur + ")")
        lignes.append("")
        lignes.append("## 📄 Licence")
        lignes.append("")
        lignes.append("Ce projet est sous licence MIT.")
        
        contenu = "\n".join(lignes)
        
        st.success("✅ README généré avec succès !")
        st.subheader("Aperçu du rendu :")
        st.markdown(contenu)
        
        st.download_button(
            label="📥 Télécharger le fichier README.md",
            data=contenu.encode('utf-8'),
            file_name="README.md",
            mime="text/markdown",
            use_container_width=True
        )

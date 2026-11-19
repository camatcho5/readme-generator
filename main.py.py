import os

def demander_question(question, defaut=""):
    """Pose une question et retourne la réponse (ou la valeur par défaut)."""
    reponse = input(f"{question} ")
    return reponse.strip() if reponse.strip() else defaut

def generer_readme():
    print("=" * 50)
    print("  GÉNÉRATEUR DE README")
    print("=" * 50)
    print("Réponds aux questions ci-dessous (appuie sur Entrée pour ignorer).\n")

    nom = demander_question("Nom du projet :", "Mon Projet")
    description = demander_question("Description courte :", "Un projet open source.")
    technologies = demander_question("Technologies (ex: Python, Flask) :", "Python")
    installation = demander_question("Commande d'installation :", "pip install -r requirements.txt")
    usage = demander_question("Exemple d'utilisation :", "python main.py")
    auteur = demander_question("Ton nom / pseudo GitHub :", "Anonyme")

    contenu = f"""# {nom}

{description}

## 🚀 Technologies

- {technologies}

## 📦 Installation

```bash
{installation}
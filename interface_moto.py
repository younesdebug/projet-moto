from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

st.title("Quelle moto choisir ?")

fichier_csv = Path(__file__).with_name("questionnaire_moto_marque_prix.csv")
donnees = pd.read_csv(fichier_csv)

questions = {
    "vitesse": "Aimes-tu les sensations de vitesse à moto ?",
    "usage_principal": "Quel est ton usage principal ?",
    "position_conduite": "Quelle position de conduite préfères-tu ?",
    "terrain": "Sur quel terrain aimerais-tu rouler le plus souvent ?",
    "priorite": "Qu’est-ce qui compte le plus pour toi ?",
}

with st.form("questionnaire_moto"):
    reponses = {}
    for colonne, question in questions.items():
        choix = sorted(donnees[colonne].unique())
        reponses[colonne] = st.selectbox(question, choix, key=colonne)
    predire = st.form_submit_button("Prédire")

if predire:
    X_encode = pd.get_dummies(donnees[list(questions)], dtype=int)
    choix_moto = donnees["marque_preferee"] + " — " + donnees["modele_reference"]

    arbre_moto = DecisionTreeClassifier(random_state=42)
    arbre_moto.fit(X_encode, choix_moto)

    profil = pd.DataFrame([reponses])
    profil_encode = pd.get_dummies(profil, dtype=int).reindex(
        columns=X_encode.columns, fill_value=0
    )
    moto_predite = arbre_moto.predict(profil_encode)[0]
    fiche = donnees.loc[choix_moto == moto_predite].iloc[0]
    prix = f"{int(fiche['prix_catalogue_dh']):,}".replace(",", " ")

    st.success(f"Moto suggérée — {moto_predite}")
    st.info(f"Prix de référence — {prix} DH")
    st.caption(fiche["nature_prix"])
    st.markdown(f"[Voir la source du prix]({fiche['source_prix_url']})")

# Projet Moto

Application de Younes Radouani qui suggère une moto à partir de cinq réponses sur les sensations de vitesse, l’usage, la position de conduite, le terrain et la priorité. Le résultat affiche la marque, le modèle et son prix de référence au Maroc avec un lien vers la source.

## Technologies utilisées

| Technologie | Utilisation |
| --- | --- |
| Python 3.13 | Développement de l’application |
| pandas | Lecture du CSV et encodage one-hot des réponses avec `get_dummies` |
| scikit-learn | Classification supervisée avec `DecisionTreeClassifier` |
| Streamlit | Formulaire web local et affichage de la recommandation |
| Google Sheets et CSV | Préparation du premier questionnaire et format des données |
| VS Code et PowerShell | Édition et exécution sur Windows |
| pip | Installation des dépendances Python |
| Git et GitHub | Gestion de versions et publication du code |

## Lancer l’application

Depuis le dossier du projet, dans le terminal de VS Code.

```powershell
python -m pip install -r requirements.txt
python -m streamlit run interface_moto.py
```

## Données et fonctionnement

Le CSV contient 192 profils simulés associés à 24 références Yamaha, KTM, Honda et SYM. Les liens vers MIFA Motors, KTM Maroc et les guides ou annonces tiers sont indiqués dans `source_prix_url`.

L’arbre utilise uniquement les cinq réponses pour prédire une paire marque–modèle. L’application récupère ensuite le prix de cette référence dans le CSV. Les prix sont des relevés indicatifs, avec leur date et leur source. Les profils simulés servent à démontrer le pipeline. La fiabilité des recommandations auprès de vrais utilisateurs reste à évaluer.

## Crédits

Projet réalisé par **[Younes Radouani](https://github.com/younesdebug)**.

# Chatbot Étudiant Intelligent

## Contexte  
Dans un environnement universitaire, les étudiants ont souvent besoin d’accéder rapidement à des informations pratiques (horaires, coordonnées des professeurs, dates d’examen, services disponibles…).  
L’objectif de ce projet est de concevoir un **chatbot thématique** capable de répondre automatiquement à ces questions, de manière structurée et interactive.  

---

## Objectifs  
- Fournir un assistant virtuel dédié aux étudiants.  
- Organiser les informations par thèmes principaux (Professeurs, Cours, Examens, Bibliothèque, Services étudiants…).  
- Permettre une interaction en plusieurs étapes : choix d’un thème → sous-question → réponse précise.  
- Créer une base de connaissances facilement extensible (au format JSON/CSV).  

---

## Outils et technologies utilisés  
- **Langage** : Python  
- **Bibliothèques** :  
  - `json` pour la gestion de la base de connaissances  
  - `scikit-learn` et `NLTK` (extensions possibles) pour le NLP  
  - `Streamlit` pour une interface web conviviale (optionnel)  
- **Organisation des données** : JSON structuré par thèmes et sous-questions  

---

## Fonctionnalités  
- Sélection d’un thème général (ex. Professeurs).  
- Choix d’une sous-question (ex. Matière enseignée, horaires de permanence, coordonnées).  
- Génération d’une réponse adaptée depuis la base de connaissances.  
- Interaction en console et possibilité d’évolution vers une interface web interactive.  
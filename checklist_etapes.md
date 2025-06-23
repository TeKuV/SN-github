# Checklist de réalisation du mini-projet IA / GitHub / Hugging Face

Coche chaque case lorsque l’étape est terminée.

## 0 – Pré-requis & environnement
[x] Installer Git et configurer le nom d’utilisateur / email.
[x] Vérifier que Python (>=3.8) et `pip` sont installés.
[ ] Créer/activer un environnement virtuel (venv, conda…).

## 1 – Création et initialisation du dépôt
[x] Créer un nouveau **dépôt public** sur GitHub.
[ ] Cloner le dépôt en local : `git clone …`.
[ ] Créer un fichier `README.md` décrivant brièvement le projet (modèle IA factice).
[ ] Ajouter un `.gitignore` adapté à un projet Python (`__pycache__/`, `*.joblib`, envs, etc.).
[ ] Écrire `model.py` avec :
    * `train_and_save_model()` qui crée & sauvegarde un modèle factice.
    * `predict()` qui charge le modèle et simule une prédiction.
[ ] Commiter ces fichiers sur la branche **main** (`git add . && git commit -m "Initial commit" && git push`).

## 2 – Stratégie de branches Git
[ ] Créer la branche **develop** à partir de `main` : `git checkout -b develop`.
[ ] Créer la branche **feature/initial-model-setup** à partir de `develop`.
[ ] Développer et commiter sur `feature/initial-model-setup` (amélioration du modèle/test).
[ ] Fusionner la branche de fonctionnalité dans **develop** (pull request ou `git merge`).
[ ] Tester & valider, puis fusionner **develop** dans **main** (pull request).

## 3 – Gestion des fichiers de modèle volumineux (si nécessaire)
[ ] Installer **Git LFS** : `git lfs install`.
[ ] Suivre les fichiers de modèle : `git lfs track "*.joblib"` (ou autre extension).
[ ] Commiter les changements de suivi LFS.

## 4 – Préparation du compte Hugging Face
[ ] Créer un compte sur Hugging Face ou se connecter.
[ ] Générer un **Access Token** HF avec scope *write*.
[ ] Créer un repository (Espace) Hugging Face pour le modèle.

## 5 – Configuration de GitHub Actions
[ ] Ajouter les secrets `HF_TOKEN` (token Hugging Face) et `EMAIL_PASSWORD` / autres secrets SMTP dans **Settings > Secrets and variables > Actions** du repo GitHub.
[ ] Créer le fichier workflow `.github/workflows/deploy.yml` contenant :
    * Étape *checkout* du code.
    * Installation de Python, dépendances et Git LFS.
    * Exécution du script `model.py` pour entraîner et sauvegarder le modèle.
    * Publication du modèle sur le repo Hugging Face via `huggingface_hub` ou `git push`.
    * Envoi d’un mail de notification après déploiement (action SMTP ou script Python utilisant les secrets).
[ ] Pousser le workflow et vérifier qu’il s’exécute correctement sur chaque push dans `main`.

## 6 – Vérification et démonstration
[ ] Vérifier que le modèle est bien visible sur Hugging Face Hub.
[ ] Vérifier la réception de l’email automatique après déploiement.
[ ] Effectuer des captures d’écran : branches, commits, workflow, dépôt HF, email.
[ ] Enregistrer une **vidéo de démonstration** (≤ 5 min) présentant oralement le dépôt, le workflow et le résultat.

## 7 – Rédaction du rapport
[ ] Créer `rapport_nom_matricule.pdf` :
    * Présentation concise du projet.
    * Captures d’écran légendées.
    * Réponses aux questions (stratégie de branches, Git LFS, etc.).
    * Contenu (ou lien) du fichier workflow `.yml`.

## 8 – Livraison
[ ] Vérifier que tout le code est poussé sur GitHub.
[ ] Créer le fichier ZIP `nom_etudiant_matricule_GIT-GITHUB.zip` contenant :
    * `rapport_nom_matricule.pdf`
    * `demo_nom_matricule.mp4` (ou lien texte)
[ ] Vérifier l’intégrité du ZIP.
[ ] Soumettre le fichier ZIP via la plateforme prévue.

---
> Bon courage ! Cocher chaque case au fur et à mesure pour suivre l’avancement.

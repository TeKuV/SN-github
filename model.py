import joblib
import os

# Définir le chemin du modèle
MODEL_PATH = 'fake_model.joblib'

def train_and_save_model():
    """Crée un modèle factice et le sauvegarde sur le disque."""
    print("Entraînement du modèle factice...")
    # Création d'un modèle simple (un dictionnaire dans ce cas)
    model = {'feature': 'valeur', 'accuracy': 0.95}
    
    print(f"Sauvegarde du modèle à l'emplacement : {MODEL_PATH}")
    joblib.dump(model, MODEL_PATH)
    print("Modèle sauvegardé.")

def predict():
    """Charge le modèle factice et simule une prédiction."""
    if not os.path.exists(MODEL_PATH):
        print("Le modèle n'existe pas. Veuillez l'entraîner d'abord.")
        return

    print("Chargement du modèle...")
    model = joblib.load(MODEL_PATH)
    print("Modèle chargé.")
    
    # Simulation d'une prédiction
    prediction = model.get('accuracy', 0) # Prédit la "précision"
    print(f"Prédiction simulée : {prediction}")
    return prediction

if __name__ == '__main__':
    train_and_save_model()
    predict()

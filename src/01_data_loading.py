import pandas as pd
import os

# Directori base del projecte (carpeta arrel)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
SAVE_PATH = os.path.join(DATA_DIR, "cleaned.csv")

# Noms de columna segons la documentació oficial
COLUMN_NAMES = [
    "Status_checking_account", "Duration_month", "Credit_history", "Purpose", "Credit_amount",
    "Savings_account", "Employment_since", "Installment_rate", "Personal_status_sex", "Debtors",
    "Residence_since", "Property", "Age", "Other_installment_plans", "Housing",
    "Existing_credits", "Job", "Dependents", "Telephone", "Foreign_worker", "Target"
]

def download_and_clean_data(url, save_path):
    print("Downloading data...")
    df = pd.read_csv(url, sep=' ', header=None)
    df.columns = COLUMN_NAMES

    df["Target"] = df["Target"].map({1: 0, 2: 1})  # 0 = good, 1 = bad (default)

    print("Data shape:", df.shape)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print("🧹 Saved cleaned dataset to:", save_path)

if __name__ == "__main__":
    download_and_clean_data(
        url="https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data",
        save_path=SAVE_PATH
    )

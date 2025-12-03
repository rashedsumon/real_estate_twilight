

## **data_loader.py** (Auto-download Kaggle datasets)


import kagglehub
import os

DATA_DIR = "data"

def download_dataset():
    os.makedirs(DATA_DIR, exist_ok=True)
    # Example dataset: irregular facades
    path = kagglehub.dataset_download("liushuyuu/irregular-facades-irfs", download_path=DATA_DIR)
    print("Dataset downloaded to:", path)
    return path

if __name__ == "__main__":
    download_dataset()

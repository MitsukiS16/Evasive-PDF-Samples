import pandas as pd
from pdf import PDF

def read_dataset(file_path):
    evasive = pd.read_csv(file_path)
    return evasive

def process_dataset(data):
    # Process the dataset as needed
    pass

def write_dataset(evasive, non_evasive):
    print(f"There is {len(evasive)}")
    print(f"There is {len(non_evasive)}")
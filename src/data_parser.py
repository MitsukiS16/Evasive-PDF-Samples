import pandas as pd
from pdf import PDF

def read_dataset(file_path):
    data = pd.read_csv(file_path)
    pdf_objects = []
    for index, row in data.iterrows():
        pdf = PDF(
            row['pdfsize'], 
            row['pages'], 
            row['title characters'], 
            row['images'], 
            row['obj'], 
            row['endobj'], 
            row['stream'], 
            row['endstream'], 
            row['xref'], 
            row['trailer'], 
            row['startxref'], 
            row['ObjStm'], 
            row['JS'], 
            row['OBS_JS'], 
            row['Javascript'], 
            row['OBS_Javascript'], 
            row['OpenAction'], 
            row['OBS_OpenAction'], 
            row['Acroform'], 
            row['OBS_Acroform'], 
            row['class']
        )
        pdf_objects.append(pdf)
    return pdf_objects


def calculateMeanPageSize(pdf_list):
    total_page_size = sum(pdf.pdfsize for pdf in pdf_list)
    mean_page_size = total_page_size / len(pdf_list)
    return int(mean_page_size)
    

def write_dataset(evasive, non_evasive):
    # Create a DataFrame with the information
    data = {
        'Type': ['Evasive', 'Non Evasive'],
        'nLines': [len(evasive), len(non_evasive)],
        'MeanPages': [calculateMeanPageSize(evasive), calculateMeanPageSize(non_evasive)]
    }
    df = pd.DataFrame(data)
    
    # Print the DataFrame
    print(df)
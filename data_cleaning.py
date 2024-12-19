import pandas as pd
import numpy as np

def clean_customer_data(file_path):
    """
    Clean and prepare customer feedback data
    """
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Convert dates
    df['feedback_date'] = pd.to_datetime(df['feedback_date'])
    
    # Clean satisfaction scores
    df['satisfaction_score'] = pd.to_numeric(df['satisfaction_score'], errors='coerce')
    
    # Standardize feedback sources
    df['source'] = df['source'].str.lower().str.strip()
    
    # Handle missing values
    df['satisfaction_score'] = df['satisfaction_score'].fillna(df['satisfaction_score'].median())
    df['comments'] = df['comments'].fillna('No comment provided')
    
    return df

if __name__ == "__main__":
    df = clean_customer_data('data/raw/customer_feedback.csv')
    df.to_csv('data/processed/cleaned_feedback.csv', index=False)
    print("Data cleaning completed!")

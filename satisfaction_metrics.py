import pandas as pd
import numpy as np

def calculate_satisfaction_metrics(df):
    """
    Calculate detailed satisfaction metrics
    """
    # Monthly trends
    monthly_scores = df.groupby(df['feedback_date'].dt.strftime('%Y-%m')).agg({
        'satisfaction_score': ['mean', 'count'],
        'feedback_id': 'count'
    })
    
    # Response rate calculation
    response_rate = (df['feedback_id'].count() / df['total_customers'].iloc[0]) * 100
    
    # Category satisfaction
    category_satisfaction = df.groupby('product_category').agg({
        'satisfaction_score': ['mean', 'count']
    }).round(2)
    
    return monthly_scores, response_rate, category_satisfaction

if __name__ == "__main__":
    df = pd.read_csv('data/processed/cleaned_feedback.csv')
    monthly, response_rate, category = calculate_satisfaction_metrics(df)
    
    # Save results
    monthly.to_csv('data/processed/monthly_satisfaction.csv')
    category.to_csv('data/processed/category_satisfaction.csv')

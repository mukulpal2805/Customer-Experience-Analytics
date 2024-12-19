import pandas as pd
import numpy as np

def analyze_feedback(df):
    """
    Analyze customer feedback and calculate metrics
    """
    # Calculate key metrics
    metrics = {
        'avg_satisfaction': df['satisfaction_score'].mean(),
        'total_responses': len(df),
        'positive_feedback': len(df[df['satisfaction_score'] >= 4]),
        'negative_feedback': len(df[df['satisfaction_score'] <= 2])
    }
    
    # Product line analysis
    product_metrics = df.groupby('product_line').agg({
        'satisfaction_score': ['mean', 'count'],
        'feedback_id': 'count'
    }).round(2)
    
    return metrics, product_metrics

if __name__ == "__main__":
    df = pd.read_csv('data/processed/cleaned_feedback.csv')
    metrics, product_analysis = analyze_feedback(df)
    
    print("\nCustomer Feedback Analysis:")
    print(f"Average Satisfaction: {metrics['avg_satisfaction']:.2f}")
    print(f"Total Responses: {metrics['total_responses']}")
    print(f"Positive Feedback: {metrics['positive_feedback']}")

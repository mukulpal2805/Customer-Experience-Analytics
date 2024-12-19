-- Overall Customer Satisfaction Analysis
SELECT 
    product_line,
    COUNT(*) as total_responses,
    AVG(satisfaction_score) as avg_satisfaction,
    COUNT(CASE WHEN satisfaction_score >= 4 THEN 1 END) as satisfied_customers,
    COUNT(CASE WHEN satisfaction_score <= 2 THEN 1 END) as unsatisfied_customers
FROM customer_feedback
GROUP BY product_line
ORDER BY avg_satisfaction DESC;

-- Monthly Trend Analysis
SELECT 
    DATE_FORMAT(feedback_date, '%Y-%m') as month,
    COUNT(*) as total_feedback,
    AVG(satisfaction_score) as avg_score,
    COUNT(DISTINCT customer_id) as unique_customers
FROM customer_feedback
GROUP BY DATE_FORMAT(feedback_date, '%Y-%m')
ORDER BY month;

-- Response Rate by Channel
SELECT 
    feedback_channel,
    COUNT(*) as responses,
    AVG(satisfaction_score) as avg_satisfaction,
    COUNT(*) * 100.0 / SUM(COUNT(*)) OVER() as response_percentage
FROM customer_feedback
GROUP BY feedback_channel
ORDER BY responses DESC;

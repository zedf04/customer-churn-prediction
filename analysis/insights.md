# Customer Churn Analysis & Insights

## Objective

The goal of this analysis is to understand the factors associated with customer churn and identify patterns that can help businesses take preventive action.

---

## Key Churn Factors

### 1. Support Calls

Customers with a higher number of support calls show a stronger association with churn.

This may indicate dissatisfaction, unresolved issues, or repeated problems with the service.

### 2. Payment Delay

Payment delay is one of the important signals associated with churn.

Customers with larger payment delays may have a higher likelihood of leaving the service.

### 3. Contract Length

Customers on shorter/monthly contracts show higher churn compared with customers on longer contracts.

Longer contracts may therefore be associated with greater customer retention.

### 4. Customer Engagement

Engagement-related behavior is useful for identifying customers who may be at higher risk of churn.

The project uses an engineered:

`Engagement Score = Usage Frequency / (Last Interaction + 1)`

Lower engagement can act as a warning signal.

### 5. Customer Spending

Total spending and spending relative to tenure provide additional information about customer behavior.

The project therefore includes:

`Spend per Tenure = Total Spend / (Tenure + 1)`

---

## Engineered Features

The model uses additional features created from the original customer data:

- High Support
- Payment Risk
- Engagement Score
- Spend per Tenure
- Is New Customer

These features were designed to capture behavioral patterns that may not be directly represented by the original variables.

---

## Business Interpretation

The analysis suggests that customers showing combinations of:

- frequent support interactions
- significant payment delays
- low engagement
- shorter contracts

may require additional retention attention.

These factors should be treated as **signals associated with churn**, rather than proof that they directly cause churn.

---

## Recommended Business Actions

### High Support Customers
Investigate unresolved customer problems and provide proactive support.

### Customers With Payment Delays
Offer payment reminders or assistance before payment issues become persistent.

### Low Engagement Customers
Use targeted engagement campaigns to encourage product usage.

### Monthly Contract Customers
Consider retention incentives or benefits for customers willing to move to longer-term contracts.

---

## Model

The project uses a Random Forest classifier for churn prediction.

### Reported Performance

- Accuracy: 93.59%
- AUC: 0.95
- Churn Precision: 0.90
- Churn Recall: 1.00
- Churn F1-Score: 0.95
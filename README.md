# Customer Retention Analysis & Churn Prediction

An end-to-end Machine Learning project that analyzes customer behavior,
identifies factors associated with churn, and predicts whether a customer
is likely to leave a service.

The trained Random Forest model is deployed through a FastAPI backend
with a web-based frontend for real-time predictions.

---

## 🎯 Project Objective

Customer churn is a major challenge for subscription-based businesses.

The goal of this project is to:

- Predict customers who are likely to churn
- Understand factors associated with customer churn
- Perform Exploratory Data Analysis (EDA)
- Engineer meaningful behavioral features
- Compare multiple Machine Learning algorithms
- Deploy the best-performing model as a web application

---

## 📊 Dataset

The project uses a customer churn dataset containing approximately
505,000 customer records.

### Main Features

- Age
- Gender
- Tenure
- Usage Frequency
- Support Calls
- Payment Delay
- Subscription Type
- Contract Length
- Total Spend
- Last Interaction

Target:

- `0` → Retained
- `1` → Churned

---

## 🔍 Exploratory Data Analysis

EDA was performed to understand customer behavior and identify patterns
associated with churn.

The analysis includes:

- Churn distribution
- Churn rate by categorical variables
- Numerical feature analysis
- Correlation analysis
- KDE plots
- Feature importance analysis

### Key Findings

- Monthly-contract customers showed significantly higher churn than
  annual-contract customers.
- Support Calls and Payment Delay showed strong relationships with churn.
- Total Spend showed a negative relationship with churn in the analysis.

---

## ⚙️ Feature Engineering

Five additional features were engineered:

| Feature | Description |
|---|---|
| High Support | Support Calls >= 5 |
| Payment Risk | Payment Delay >= 20 |
| Engagement Score | Usage Frequency / (Last Interaction + 1) |
| Spend per Tenure | Total Spend / (Tenure + 1) |
| Is New Customer | Tenure <= 6 |

These features were created to capture additional behavioral patterns
from the original customer attributes.

---

## 🤖 Machine Learning Models

Three classification algorithms were evaluated:

1. Logistic Regression
2. Random Forest
3. XGBoost

### Model Comparison

| Model | Accuracy | AUC | Churn Recall | Churn F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | 84.42% | — | — | — |
| Random Forest | **93.59%** | **0.95** | **100%** | **0.95** |
| XGBoost | 93.40% | — | — | — |

### Best Model

**Random Forest Classifier**

The Random Forest model achieved the highest reported accuracy of
**93.59%**, with an **AUC of 0.95** and **100% recall for the churned
class**.

---

## 📈 Important Churn Signals

Random Forest feature importance identified several important signals:

1. Support Calls
2. Total Spend
3. High Support
4. Age
5. Payment Delay

These should be interpreted as **model signals associated with churn**,
not proof of direct causation.

---

## 🌐 Web Application

The trained model is deployed using **FastAPI**.

### Application Flow

```text
Customer Input
      ↓
FastAPI API
      ↓
Feature Engineering
      ↓
Feature Scaling
      ↓
Random Forest Model
      ↓
Churn Probability
      ↓
Risk Level
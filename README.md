# Customer Retention Analysis & Churn Prediction

An end-to-end Machine Learning project that analyzes customer behavior and predicts whether a customer is likely to churn.

The project combines Exploratory Data Analysis (EDA), feature engineering, multiple machine learning models, model evaluation, and a FastAPI web application for real-time churn prediction.

---

## 📌 Project Overview

Customer churn is an important problem for subscription-based businesses. Identifying customers who are at higher risk of leaving can help businesses take proactive retention actions.

This project aims to:

- Analyze customer behavior and churn patterns
- Perform exploratory data analysis
- Engineer meaningful features for churn prediction
- Train and compare multiple machine learning models
- Identify important signals associated with customer churn
- Select the best-performing model
- Deploy the trained model using FastAPI
- Provide a web interface for real-time churn predictions

---

## 🎯 Objectives

The main objectives of this project are:

1. Predict whether a customer is likely to churn.
2. Analyze behavioral and financial patterns associated with churn.
3. Perform data preprocessing and feature engineering.
4. Compare different machine learning algorithms.
5. Select the best-performing model.
6. Evaluate the selected model using classification metrics and ROC-AUC.
7. Deploy the model as a web application.

---

## 📊 Dataset

The project uses a customer churn dataset containing more than 500,000 customer records.

The dataset is divided into training and testing CSV files and is located inside:

```text
analysis/datasets/
```

### Features

| Feature | Description |
|---|---|
| Age | Customer age |
| Gender | Customer gender |
| Tenure | Number of months as a customer |
| Usage Frequency | Frequency of service usage |
| Support Calls | Number of support calls made |
| Payment Delay | Number of days payment was delayed |
| Subscription Type | Basic / Standard / Premium |
| Contract Length | Monthly / Quarterly / Annual |
| Total Spend | Total amount spent by the customer |
| Last Interaction | Days since last interaction |
| Churn | Target variable: 0 = Retained, 1 = Churned |

---

## 🔍 Exploratory Data Analysis

The project includes extensive Exploratory Data Analysis (EDA), including:

- Churn distribution analysis
- Categorical feature analysis
- Churn rate comparisons
- Numerical feature distributions
- KDE plots
- Correlation analysis
- Feature relationship analysis

### Key Observations

Some important patterns identified during the analysis include:

- Monthly-contract customers show higher churn compared with longer-term contracts.
- Support Calls show a strong relationship with churn.
- Payment Delay is strongly associated with churn.
- Total Spend shows a negative relationship with churn.
- Customer engagement-related variables provide useful signals for distinguishing churned and retained customers.

> These findings represent patterns and associations in the dataset and should not be interpreted as proof that a particular feature directly causes churn.

---

## ⚙️ Feature Engineering

Five additional features were created to provide the models with more meaningful customer-level signals.

### 1. High Support

```text
Support Calls >= 5 → 1
Otherwise → 0
```

Identifies customers with relatively high support interaction.

### 2. Payment Risk

```text
Payment Delay >= 20 → 1
Otherwise → 0
```

Identifies customers with significant payment delays.

### 3. Engagement Score

```text
Usage Frequency / (Last Interaction + 1)
```

Combines usage frequency with recent customer interaction.

### 4. Spend per Tenure

```text
Total Spend / (Tenure + 1)
```

Provides a normalized measure of customer spending relative to tenure.

### 5. Is New Customer

```text
Tenure <= 6 → 1
Otherwise → 0
```

Identifies relatively new customers.

---

## 🤖 Machine Learning Models

Three classification algorithms were trained and evaluated.

### Logistic Regression

Used as a baseline classification model.

**Accuracy:** 84.42%

---

### Random Forest

Random Forest was selected as the final model because it performed best among the evaluated models.

The model uses an ensemble of decision trees to capture non-linear relationships within the customer data.

**Accuracy:** 93.59%

**AUC:** 0.9523

**Churn Recall:** 100%

**Churn F1:** 0.95

---

### XGBoost

XGBoost was also evaluated as a powerful gradient boosting algorithm for structured/tabular data.

**Accuracy:** 93.40%

---

## 📈 Model Comparison

| Model | Accuracy | AUC | Churn Recall | Churn F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | 84.42% | — | — | — |
| Random Forest | **93.59%** | **0.9523** | **100%** | **0.95** |
| XGBoost | 93.40% | — | — | — |

### 🏆 Selected Model

**Random Forest**

The Random Forest model achieved the highest accuracy among the evaluated models and achieved **100% recall for churned customers** on the test set.

---

## 📋 Random Forest Classification Report

The Random Forest model was evaluated on **101,042 test samples**.

| Class | Precision | Recall | F1-Score | Support |
|---|---:|---:|---:|---:|
| Retained | 1.00 | 0.86 | 0.92 | 44,943 |
| Churned | 0.90 | **1.00** | **0.95** | 56,099 |

**Overall Accuracy:** 93.59%

### Interpretation

The model achieved **100% recall for the Churned class**, meaning that in this test set it did not miss any actual churned customers.

For a churn detection system, high recall can be particularly useful because missing a customer who is likely to churn may reduce the opportunity for proactive retention.

---

## 📉 ROC-AUC Evaluation

The Random Forest achieved:

```text
AUC = 0.9523
```

The ROC curve evaluates the model's ability to distinguish between retained and churned customers across different classification thresholds.

An AUC close to 1 indicates strong discriminatory performance.

The complete ROC curve and evaluation are available in:

```text
analysis/CRCA_project.ipynb
```

---

## 🔎 Important Churn Signals

The analysis and model identified several features that are strongly associated with customer churn.

Important signals include:

- Support Calls
- Total Spend
- High Support
- Age
- Payment Delay
- Contract Length
- Customer engagement

The model considers these features together rather than relying on a single variable.

> Feature importance and statistical association should not be interpreted as proof of causality.

---

## 🌐 Web Application

The trained Random Forest model is deployed using **FastAPI**.

The application provides a simple web interface where users can enter customer information and receive:

- Churn prediction
- Churn probability
- Risk level
- Model performance metrics

---

## 🚦 Risk Classification

The application converts the predicted churn probability into three risk categories.

```text
Probability >= 70% → High Risk

Probability >= 40% → Medium Risk

Probability < 40% → Low Risk
```

For example:

```text
Churn Probability: 74%

Risk Level: High Risk
```

The probability represents the model's estimated likelihood based on the patterns learned from the training data.

---

## 🔄 Application Flow

```text
Customer Input
      ↓
Feature Engineering
      ↓
Feature Scaling
      ↓
Random Forest Model
      ↓
Churn Prediction
      ↓
Probability + Risk Level
```

---

## 🖥️ Application Interface

The web application contains:

### Customer Details

Users can enter:

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

### Prediction Result

The application displays:

- Prediction
- Churn Probability
- Risk Level

### Model Performance

The application also displays:

- Accuracy
- AUC Score
- F1 Score
- Selected Model

---

## 📁 Project Structure

```text
customer-churn-prediction/
│
├── analysis/
│   ├── CRCA_project.ipynb
│   ├── insights.md
│   └── datasets/
│       ├── customer_churn_dataset-testing-master.csv
│       └── customer_churn_dataset-training-master.csv
│
├── static/
│   └── index.html
│
├── main.py
├── model.pkl
├── scaler.pkl
├── features.json
├── requirements.txt
├── test.py
├── .gitignore
└── README.md
```

> **Note:** `model.pkl` is not stored directly in the Git repository because the trained model is approximately 466 MB and exceeds GitHub's standard repository file-size limit.

---

## 📦 Trained Model

The trained Random Forest model is provided separately as a GitHub Release asset.

### Download Model

[Download `model.pkl` from Release v1.0.0](../../releases/tag/v1.0.0)

After downloading the model, place it in the project root:

```text
customer-churn-prediction/
│
├── model.pkl
├── scaler.pkl
├── features.json
├── main.py
└── ...
```

The downloaded `model.pkl` is required to run the FastAPI prediction application.

---

## 🛠️ Technologies Used

### Programming

- Python
- HTML
- CSS
- JavaScript

### Machine Learning

- Scikit-learn
- XGBoost
- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Deployment

- FastAPI
- Uvicorn
- Joblib

### Development

- Jupyter Notebook
- Git
- GitHub

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/zedf04/customer-churn-prediction.git
```

Navigate into the project:

```bash
cd customer-churn-prediction
```

---

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you want to reproduce the XGBoost training from the notebook, make sure XGBoost is installed:

```bash
pip install xgboost
```

---

### 4. Download the Trained Model

Download:

```text
model.pkl
```

from the GitHub Release:

```text
v1.0.0
```

Place it in the project root directory.

---

### 5. Start the FastAPI Application

```bash
python -m uvicorn main:app --reload
```

---

### 6. Open the Web Application

Visit:

```text
http://127.0.0.1:8000
```

---

## 📚 API Endpoints

### `GET /`

Loads the web application.

---

### `POST /predict`

Accepts customer information and returns a churn prediction.

Example response:

```json
{
  "churn": 1,
  "probability": 74.0,
  "risk": "High Risk"
}
```

Where:

```text
churn = 0 → Retained
churn = 1 → Churned
```

---

### `GET /metrics`

Returns model performance information including:

- Accuracy
- AUC score
- Churn precision
- Churn recall
- Churn F1 score
- Model name
- Number of features
- Training sample count

---

## 🧪 Machine Learning Workflow

The complete machine learning workflow is available in:

```text
analysis/CRCA_project.ipynb
```

The notebook contains:

1. Data loading
2. Data cleaning
3. Data preprocessing
4. Exploratory Data Analysis
5. Feature engineering
6. Logistic Regression
7. Random Forest
8. XGBoost
9. Classification reports
10. Confusion matrix
11. ROC curve
12. AUC evaluation
13. Feature importance
14. Model predictions

---

## 📊 Model Performance Summary

```text
Random Forest

Accuracy       : 93.59%
AUC            : 0.9523
Churn Precision: 90%
Churn Recall   : 100%
Churn F1       : 0.95
```

The model was evaluated on **101,042 test samples**.

---

## 💡 Key Takeaway

This project demonstrates an end-to-end Machine Learning workflow:

```text
Raw Customer Data
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Model Training
       ↓
Model Comparison
       ↓
Random Forest Selection
       ↓
Model Evaluation
       ↓
FastAPI Deployment
       ↓
Real-Time Churn Prediction
```

The final Random Forest model achieved:

- **93.59% accuracy**
- **0.9523 AUC**
- **100% churn recall**
- **0.95 churn F1-score**

on the test set.

---

## 🔮 Future Improvements

Possible future improvements include:

- Hyperparameter tuning
- SHAP/LIME-based explainable AI
- Integration with CRM systems
- Real-time churn monitoring
- Customer segmentation
- Survival analysis to predict when a customer may churn
- Advanced deep learning approaches
- Automated retention recommendations
- Model monitoring and retraining pipelines

---

## 👨‍💻 Author

**Sagnik Ghosh**

B.Tech Computer Science & Engineering — Data Science

GitHub: [@zedf04](https://github.com/zedf04)

---

## ⭐ Project

If you find this project useful or interesting, consider giving the repository a star.

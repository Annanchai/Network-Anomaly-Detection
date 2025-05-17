# Network Anomaly Detection using Machine Learning

This project aims to build a robust anomaly detection system for network traffic using machine learning models. It involves detailed Exploratory Data Analysis (EDA), hypothesis testing, feature engineering, model building, evaluation, and deployment as an API.

---

## Problem Statement

With growing cyber threats, detecting abnormal behavior in network traffic is critical to securing systems and preventing data breaches. This project focuses on identifying such **anomalies** in network data using supervised learning techniques.

---

## Objective

- To build a classification model that can detect network anomalies with high accuracy.
- To understand key drivers behind network anomalies through EDA and hypothesis testing.
- To deploy the model as a web service for real-time inference.

---

## Target Metric

We focus on achieving a high **F1-score** to balance between precision and recall, as both false positives and false negatives are costly in network anomaly detection.

---

## Project Workflow

1. **Exploratory Data Analysis (EDA)**

   - Univariate and bivariate analysis
   - Class distribution analysis
   - Outlier detection and visualization

2. **Hypothesis Testing**

   - T-tests and Chi-square tests to validate assumptions
   - Identify features statistically linked to anomalies

3. **Data Preprocessing**

   - Encoding for categorical variables
   - Feature scaling and null value treatment

4. **Modeling**

   - Logistic Regression
   - Random Forest
   - XGBoost

5. **Model Evaluation**

   - Accuracy, Precision, Recall, F1-score
   - Confusion Matrix and ROC-AUC analysis

6. **Model Deployment**
   - Flask API to serve the trained model
   - Simple HTML frontend or API endpoint for testing

---

## Final Results

- **Best Model**: XGBoost
- **Accuracy**: 99.94%
- **Precision**: 99%
- **Recall**: 99%
- **F1 Score**: 99%

---

## Deployment

- The model is deployed as a Flask API.
- Input features are provided via a JSON payload.
- Output: Predicted class (Normal / Attack)

---

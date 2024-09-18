# Machine Learning Projects Repository
This repository contains three major machine learning projects I worked on during my CodSoft internship and studies. Each project demonstrates a different machine learning problem and solution, using real-world datasets and popular libraries like Scikit-learn, TensorFlow, and Pandas.

Projects Overview
1. SMS Spam Classification
Description: A machine learning model to classify SMS messages as either spam or not spam.
Technologies Used: Python, Scikit-learn, Natural Language Processing (NLP), CountVectorizer, TF-IDF.
Objective: Identify and filter out spam messages using text classification.
Dataset: A public dataset of SMS messages, labeled as spam or ham (not spam).
Key Features:
Data preprocessing (cleaning, tokenization)
TF-IDF vectorization for feature extraction
Naive Bayes, SVM, and Logistic Regression for classification
Model evaluation using accuracy, precision, recall, and F1-score

3. Credit Card Fraud Detection
Description: A machine learning project aimed at detecting fraudulent transactions in a credit card dataset.
Technologies Used: Python, Scikit-learn, Pandas, Matplotlib.
Objective: Build a model to detect fraudulent credit card transactions.
Dataset: An anonymized dataset containing credit card transactions with labels indicating fraudulent or non-fraudulent behavior.
Key Features:
Data balancing using undersampling/oversampling
Feature scaling and engineering
Random Forest, Decision Tree, and Logistic Regression models
Model evaluation using confusion matrix, ROC curve, and AUC score

5. Customer Churn Prediction
Description: A machine learning model to predict customer churn (whether a customer will leave or stay).
Technologies Used: Python, Scikit-learn, Pandas, Matplotlib.
Objective: Predict which customers are likely to churn, based on customer data.
Dataset: A dataset containing customer demographic and usage information.
Key Features:
Data preprocessing (handling missing values, encoding categorical variables)
Feature selection and scaling
Classification algorithms (Logistic Regression, Random Forest)
Evaluation using precision, recall, F1-score, and ROC curve

# How to Run the Projects

1. git clone https://github.com/priyansh985/CODSOFT_Internship.git
2. cd CODSOFT_Internship/<project-folder> ex: ("/sms-detection")
3. pip install -r requirements.txt note: use the specific requirements.txt for each project


# Project Structure

CODSOFT_Internship/
│
├── sms_spam_classification/
│   ├── data/
│   ├── models/
│   └── sms_spam_classification.ipynb
│
├── credit_card_fraud_detection/
│   ├── data/
│   ├── models/
│   └── credit_card_fraud_detection.ipynb
│
├── customer_churn_prediction/
│   ├── data/
│   ├── models/
│   └── customer_churn_prediction.ipynb
│
└── README.md

# License
This repository is licensed under the MIT License.

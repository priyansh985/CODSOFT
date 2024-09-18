import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
label_encoder = LabelEncoder()
scaler = StandardScaler()

model = pickle.load(open('churn_prediction.pkl','rb'))
df = pd.read_csv("churn.csv")

st.title("Customer Churn Prediction Using Logistic Regression for Classification")
gender = st.selectbox("Select Gender",options=['Female','Male'])
SeniorCitizen = st.text_input("Your you a senior citizen values between 0 and 1")
Partner = st.selectbox("Do you have partner?", options=['Yes','No'])
Dependents	 = st.selectbox("Are you dependents on other?", options=['Yes','No'])
tenure = st.text_input("Enter Your tenure?")
PhoneService = st.selectbox("Do have phone service?",options=['Yes','No'])
MultipleLines = st.selectbox("Do you have mutlilines servics?", options=['Yes','No','no phone service'])
Contract = st.selectbox("Your Contracts?",options=['One year','Two year','Month-to_month'])
TotalCharges = st.text_input("Enter your Total charges?")


def prediction(gender,Seniorsitizen,Partner,Dependents,tenure,Phoneservice,multiline,contact,totalcharge):
    data = {
    'gender': [gender],
    'SeniorCitizen': [Dependents],
    'Partner': [Partner],
    'Dependents': [Phoneservice],
    'tenure': [tenure],
    'PhoneService': [Phoneservice],
    'MultipleLines': [multiline],
    'Contract': [contact],
    'TotalCharges': [totalcharge]
    }
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)


    # Encode the categorical columns
    categorical_columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'Contract']
    for column in categorical_columns:
        df[column] = label_encoder.fit_transform(df[column])
    df = scaler.fit_transform(df)

    result = model.predict(df).reshape(1,-1)
    return result[0]


if st.button("Predict churn or not"):
    result = prediction(gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, Contract,TotalCharges)
    if result == 1:
        st.title("Churn")
    else:
        st.title('Not Churn')

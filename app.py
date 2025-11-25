import streamlit as st
import numpy as np
import pickle

# loaded_model = pickle.load(open('trained_model.sav', 'rb'))
loaded_model = pickle.load(open('D:\Study\Machine Learning\Loan_Eli\trained_model.sav', 'rb'))


st.title("Loan Eligibility System")

st.write("Provide the applicant details below to check loan eligibility")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])

applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0)
loan_term = st.number_input("Loan Amount Term (in days)", min_value=0.0)

credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

gender = 1 if gender=="Male" else 0

married = 1 if married=="Yes" else 0

dependents = 4 if dependents=="3+" else int(dependents)

education = 1 if education=="Graduate" else 0

self_employed = 1 if self_employed=="Yes" else 0

if property_area == "Rural":
    property_area = 0
elif property_area == "Semiurban":
    property_area = 1
else:
    property_area = 2


if st.button("Predict Loan Status"):
    input_data = np.array([gender, married, dependents, education, self_employed,
                           applicant_income, coapplicant_income,
                           loan_amount, loan_term,
                           credit_history, property_area]).reshape(1, -1)

    prediction = loaded_model.predict(input_data)

    if prediction[0] == 1:
            st.success("Loan is likely to be APPROVED!")
    else:
        st.error(" Loan is likely to be REJECTED.")
import numpy as np
import pickle

# Load the saved model
loaded_model = pickle.load(open('D:\Study\Machine Learning\Loan_Eli\trained_model.sav', 'rb'))

def loan_prediction(input_data):

    # Convert the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Prediction
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 1:
        return "Loan will be Approved ✔"
    else:
        return "Loan will NOT be Approved ❌"

# Example input (Replace with real values)
# Order must be EXACTLY SAME as your training features:
# ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome',
#  'CoapplicantIncome', 'LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']

example_input = (1,1,2,1,0,5000,2000,116,360,1,2)

result = loan_prediction(example_input)
print(result)

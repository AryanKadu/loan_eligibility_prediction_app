# Loan Eligibility Predictor

Interactive Streamlit app that scores loan applications using a pre-trained
machine-learning model (`trained_model.sav`). Users supply demographic and
financial details, and the app responds with an approval likelihood in real
time.

## Project Structure
- `app.py` – Streamlit UI that loads the saved model and serves predictions.
- `predict.py` – Lightweight helper script showing how to call the model from
  Python code.
- `dataset.csv` – Training dataset (not modified by the app).
- `trained_model.sav` – Serialized scikit-learn pipeline used by both scripts.

## Prerequisites
- Python 3.8+
- Recommended packages:
  - `streamlit`
  - `numpy`
  - `scikit-learn` (only if you need to retrain or inspect the model)

Install dependencies (adjust as needed):
```
pip install -r requirements.txt
```
or
```
pip install streamlit numpy scikit-learn
```

## Run Locally
From the project root:
```
streamlit run app.py
```
Streamlit will print a local URL (typically http://localhost:8501) where you
can use the app.

## Using the Model Programmatically
`predict.py` demonstrates how to pass feature values in the exact order expected
by the model and interpret the returned label. Adapt it if you want to integrate
the predictor into another service or batch-scoring workflow.

## Notes
- Ensure `trained_model.sav` stays alongside the scripts so it can be loaded.
- Do not edit `dataset.csv` in place if you plan to retrain; keep a backup.
- For deployment, consider adding input validation and authentication as needed.


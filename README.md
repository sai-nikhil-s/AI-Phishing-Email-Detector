# 🛡️ AI Phishing Email Detector 


A simple machine-learning based application that classifies email messages as
**Phishing** or **Likely Legitimate**.

The project uses Natural Language Processing (NLP) with TF-IDF feature
extraction and a Logistic Regression classifier. A Streamlit web interface
allows users to analyze email content in real time.

## Features

- Classifies emails as Phishing or Likely Legitimate
- Displays prediction confidence
- Shows legitimate and phishing probabilities
- Simple Streamlit web interface
- Machine-learning based text classification
- Lightweight and easy to run locally

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Streamlit
- Joblib

## How It Works

```text
Email Text
    ↓
Text Preprocessing
    ↓
TF-IDF Feature Extraction
    ↓
Logistic Regression
    ↓
Prediction
    ↓
Phishing / Legitimate

## Project Structure
AI-Phishing Email Detector/
│
├── app.py
├── train_model.py
├── generate_dataset.py
├── dataset.csv
├── phishing_model.pkl
├── requirements.txt
├── README.md
└── venv/


Installation

Clone or download the project and open the project folder in a terminal.

Create and activate a virtual environment:

python -m venv venv

Windows PowerShell:

.\venv\Scripts\Activate.ps1

Install the required packages:

pip install -r requirements.txt
Train the Model

To generate the dataset:

python generate_dataset.py

Then train the machine-learning model:

python train_model.py

The trained model will be saved as:

phishing_model.pkl
Run the Application

Start the Streamlit application:

streamlit run app.py

Then open the local URL shown in the terminal, usually:

http://localhost:8501
Model

The project uses:

TF-IDF (Term Frequency-Inverse Document Frequency)

to convert email text into numerical features.

A Logistic Regression classifier then uses these features to classify the email.

Dataset

The current development dataset contains 200 example emails:

100 legitimate emails
100 phishing emails

The dataset is intended for learning and demonstration purposes.

The initial dataset produced a 100% accuracy result on the held-out test set. This should not be interpreted as real-world phishing detection accuracy because the development dataset is small and template-based.

Disclaimer

This project is an educational cybersecurity project and should not be
considered a replacement for professional email security systems.



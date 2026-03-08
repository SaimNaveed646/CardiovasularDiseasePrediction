# CardiovasularDiseasePrediction

A Python-based project to predict cardiovascular disease risk using machine learning models with a FastAPI backend and a modular structure for easy deployment.

---

## **Project Overview**

This project aims to predict cardiovascular disease risk based on patient data. It provides:

- A **machine learning model** trained to predict disease risk.
- A **FastAPI backend** to serve predictions via an API.
- Modular folder structure:
  - `fastapi/` → FastAPI application files
  - `models/` → Trained ML models
  - `data/` → (Optional) datasets used for training
  - `myenv/` → Python virtual environment (ignored in Git)
  
---

## **Features**

- Predict cardiovascular risk from input features.
- Returns both **prediction** and **confidence score**.
- Easy integration with front-end applications.
- Uses **FastAPI** for fast and asynchronous API endpoints.

- CardiovasularDiseasePrediction/
│
├── fastapi/ # FastAPI backend
│ ├── main.py
│ ├── app.py
│ ├── models.py
│ ├── schemas.py
│ ├── services.py
│ ├── requirements.txt
│ └── model.pkl # Trained ML model
│
├── data/ # Dataset files (if any)
├── models/ # Optional: additional ML models
├── myenv/ # Virtual environment (ignored)
├── .gitignore
└── README.md

---

## **Installation**

**Clone the repository:**
git clone https://github.com/SaimNaveed646/CardiovasularDiseasePrediction.git
cd CardiovasularDiseasePrediction

**Set up virtual environment**
python -m venv myenv
myenv\Scripts\activate

**Install dependencies**

pip install -r fastapi/requirements.txt
Running the FastAPI Backend
cd fastapi
uvicorn main:app --reload
streamlit run frontend.py

The API will run at: http://127.0.0.1:8000
Check docs at: http://127.0.0.1:8000/docs

---



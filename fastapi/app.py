from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import pickle

from db import get_db, create_table
from sqlalchemy.orm import Session
from schemas import UserInput
from services import save_user_input

# Load ML model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()
create_table()  # Ensure table exists

@app.post("/predict")
def predict_premium(data: UserInput, db: Session = Depends(get_db)):

    # Name validation
    if not data.name.strip():
        raise HTTPException(status_code=400, detail="Name is required!")

    # Prepare ML input
    input_df = pd.DataFrame([{
        "gender": data.genderr,
        "ap_hi": data.ap_hi,
        "ap_lo": data.ap_lo,
        "cholesterol": data.cholesterol,
        "gluc": data.gluc,
        "smoke": data.smoke,
        "alco": data.alco,
        "active": data.active,
        "BMI_Category": data.bmi_category,
        "age_group": data.age_group
    }])

    # Prediction
    prediction = int(model.predict(input_df)[0])

    # Save user input + prediction to DB
    save_user_input(db, data, prediction=prediction, name=data.name.strip())

    # Return result
    return JSONResponse(
        status_code=200,
        content={"predicted_category": prediction}
    )
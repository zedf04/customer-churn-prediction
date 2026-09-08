from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib, json, numpy as np, pandas as pd
from pathlib import Path

app = FastAPI(title="Churn Prediction API")

# ── Always load from same folder as main.py ──
BASE_DIR = Path(__file__).parent

model  = joblib.load(BASE_DIR / "model.pkl")
scaler = joblib.load(BASE_DIR / "scaler.pkl")
with open(BASE_DIR / "features.json") as f:
    FEATURES = json.load(f)

# ── Schemas ──────────────────────────────────────────────
class Customer(BaseModel):
    Age: float
    Gender: int              # 0=Female, 1=Male
    Tenure: float
    Usage_Frequency: float
    Support_Calls: float
    Payment_Delay: float
    Subscription_Type: int   # 0=Basic, 1=Premium, 2=Standard
    Contract_Length: int     # 0=Annual, 1=Monthly, 2=Quarterly
    Total_Spend: float
    Last_Interaction: float

# ── Helper ───────────────────────────────────────────────
def build_features(c: dict) -> pd.DataFrame:
    c["High Support"]     = 1 if c["Support_Calls"] >= 5 else 0
    c["Payment Risk"]     = 1 if c["Payment_Delay"] >= 20 else 0
    c["Engagement Score"] = c["Usage_Frequency"] / (c["Last_Interaction"] + 1)
    c["Spend per Tenure"] = c["Total_Spend"] / (c["Tenure"] + 1)
    c["Is New Customer"]  = 1 if c["Tenure"] <= 6 else 0

    row = {
        "Age":              c["Age"],
        "Gender":           c["Gender"],
        "Tenure":           c["Tenure"],
        "Usage Frequency":  c["Usage_Frequency"],
        "Support Calls":    c["Support_Calls"],
        "Payment Delay":    c["Payment_Delay"],
        "Subscription Type": c["Subscription_Type"],
        "Contract Length":  c["Contract_Length"],
        "Total Spend":      c["Total_Spend"],
        "Last Interaction": c["Last_Interaction"],
        "High Support":     c["High Support"],
        "Payment Risk":     c["Payment Risk"],
        "Engagement Score": c["Engagement Score"],
        "Spend per Tenure": c["Spend per Tenure"],
        "Is New Customer":  c["Is New Customer"]
    }
    return pd.DataFrame([row])[FEATURES]

def risk_label(prob):
    if prob >= 0.7: return "High Risk"
    if prob >= 0.4: return "Medium Risk"
    return "Low Risk"

# ── Routes ───────────────────────────────────────────────
@app.get("/")
def index():
    return FileResponse(BASE_DIR / "static/index.html")

@app.post("/predict")
def predict(customer: Customer):
    df = build_features(customer.dict())

    # Apply the same scaling used during model training
    df_scaled = scaler.transform(df)

    prob = float(model.predict_proba(df_scaled)[0][1])
    pred = int(model.predict(df_scaled)[0])

    return {
        "churn": pred,
        "probability": round(prob * 100, 2),
        "risk": risk_label(prob)
    }

@app.get("/metrics")
def metrics():
    return {
        "accuracy": 0.9359,
        "auc_score": 0.9523,
        "precision_churned": 0.90,
        "recall_churned": 1.00,
        "f1_churned": 0.95,
        "model": "Random Forest",
        "features": len(FEATURES),
        "training_samples": 440832
    }

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

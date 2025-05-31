from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from utils import mask_pii
import joblib
import os
from dummy_classifier import DummyClassifier

app = FastAPI(title="Email Classification API")

# Load the trained model
try:
    model = joblib.load('email_classifier.joblib')
except:
    raise RuntimeError("Model file not found. Please train the model first.")

class EmailRequest(BaseModel):
    email_content: str

class EmailResponse(BaseModel):
    classification: str
    masked_content: str
    entities: Dict[str, List[str]]

@app.post("/classify", response_model=EmailResponse)
async def classify_email(request: EmailRequest):
    try:
        # Mask PII in the email content
        masked_content, entities = mask_pii(request.email_content)
        
        # Classify the email
        classification = model.predict([masked_content])[0]
        
        response = EmailResponse(
            classification=classification,
            masked_content=masked_content,
            entities=entities
        )
        
        print("API Response:", response)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
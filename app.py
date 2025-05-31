from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from dummy_classifier import DummyClassifier
from utils import mask_pii

app = FastAPI(
    title="Email Classification API",
    description="API for classifying emails and extracting PII",
    version="1.0.0"
)

# Initialize the dummy classifier
classifier = DummyClassifier()

class EmailRequest(BaseModel):
    email_content: str

class EmailResponse(BaseModel):
    classification: str
    masked_content: str
    entities: Dict[str, List[str]]

@app.get("/")
async def read_root():
    return {"message": "Email Classification API is running"}

@app.post("/classify", response_model=EmailResponse)
async def classify_email(request: EmailRequest):
    try:
        # Classify the email using the predict method
        classification = classifier.predict([request.email_content])[0]
        
        # Mask PII and extract entities
        masked_content, entities = mask_pii(request.email_content)
        
        return EmailResponse(
            classification=classification,
            masked_content=masked_content,
            entities=entities
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# This file is needed for Hugging Face Spaces deployment
# It simply imports the FastAPI app from main.py 
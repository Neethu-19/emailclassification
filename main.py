from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
import uvicorn
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

@app.post("/classify", response_model=EmailResponse)
async def classify_email(request: EmailRequest):
    try:
        # Classify the email
        classification = classifier.classify(request.email_content)
        
        # Mask PII and extract entities
        masked_content, entities = mask_pii(request.email_content)
        
        return EmailResponse(
            classification=classification,
            masked_content=masked_content,
            entities=entities
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
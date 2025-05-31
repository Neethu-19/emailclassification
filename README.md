---
title: Email Classification API
emoji: 📧
colorFrom: blue
colorTo: indigo
sdk: docker
sdk_version: 3.1.0
app_file: app.py
pinned: false
---

# Email Classification API

This is a FastAPI-based API for classifying emails and extracting PII (Personally Identifiable Information).

## Features

- Email classification into categories (Incident, Request, Change, Problem)
- PII detection and masking
- Entity extraction
- RESTful API interface

## API Endpoints

### POST /classify
Classifies an email and returns the classification, masked content, and extracted entities.

**Request Body:**
```json
{
    "email_content": "Your email content here"
}
```

**Response:**
```json
{
    "classification": "string",
    "masked_content": "string",
    "entities": {
        "emails": ["string"],
        "names": ["string"],
        "phone_numbers": ["string"]
    }
}
```

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python main.py
   ```
4. Access the API documentation at `http://localhost:8001/docs`

## Hugging Face Spaces Deployment

This API is deployed on Hugging Face Spaces. You can access it at:
https://neethu19-emailclassification.hf.space 
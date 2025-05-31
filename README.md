# Email Classification API

This FastAPI application classifies emails into predefined categories (Incident, Request, Change, Problem) and masks PII/PCI data.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Train the model:
```bash
python models.py
```

3. Run the API:
```bash
python main.py
```

## API Usage

Send a POST request to `/classify` with the following JSON format:

```json
{
    "email_content": "Your email content here"
}
```

The API will return:
```json
{
    "classification": "category",
    "masked_content": "email content with PII masked",
    "entities": {
        "entity_type": ["masked_value1", "masked_value2"]
    }
}
```

## Deployment

The application is configured for deployment on Hugging Face Spaces. The API will be available at the provided endpoint. 
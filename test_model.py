import joblib
from utils import mask_pii
from dummy_classifier import DummyClassifier

def test_model():
    try:
        # Load the model
        print("Loading model...")
        model = joblib.load('email_classifier.joblib')
        print("Model loaded successfully!")

        # Test email with PII
        test_email = """
        Hello Support Team,
        My name is John Smith and I need help with my account.
        You can reach me at john.smith@email.com or call me at +1-555-123-4567.
        My credit card number is 4111-1111-1111-1111.
        """

        # Test masking
        print("\nTesting PII masking...")
        masked_content, entities = mask_pii(test_email)
        print("Masked content:", masked_content)
        print("Detected entities:", entities)

        # Test classification
        print("\nTesting classification...")
        prediction = model.predict([masked_content])[0]
        print("Predicted category:", prediction)

        print("\nAll tests passed successfully!")
        return True

    except Exception as e:
        print(f"Error during testing: {str(e)}")
        return False

if __name__ == "__main__":
    result = test_model()
    if not result:
        exit(1) 
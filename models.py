from typing import List
import random
import joblib
from dummy_classifier import DummyClassifier

class DummyClassifier:
    def predict(self, X):
        categories = ["Incident", "Request", "Change", "Problem"]
        return [random.choice(categories) for _ in X]

# Create and save the dummy classifier
classifier = DummyClassifier()
joblib.dump(classifier, 'email_classifier.joblib')
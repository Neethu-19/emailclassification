import random

class DummyClassifier:
    def predict(self, X):
        categories = ["Incident", "Request", "Change", "Problem"]
        return [random.choice(categories) for _ in X] 
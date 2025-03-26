from transformers import pipeline

class Classifier:
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification",
                                   model="facebook/bart-large-mnli")

    def classify_text(self, text: str, labels: list) -> dict:
        result = self.classifier(text, labels)
        return {
            "type": result['labels'][0],
            "sub_type": result['labels'][1] if len(result['labels']) > 1 else "Unknown"
        }

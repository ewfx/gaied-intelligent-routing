from fastapi import FastAPI
from classifier import classify_request
from extractor import extract_key_data
from rules import route_request

app = FastAPI()

@app.post("/process-email")
async def process_email(email_body: str):
    # Classify the email
    classification = classify_request(email_body)
    
    # Extract key data
    key_data = extract_key_data(email_body)
    
    # Route the request to the appropriate team
    route = route_request({"Request Type": classification})

    return {
        "classification": classification,
        "key_data": key_data,
        "route": route
    }

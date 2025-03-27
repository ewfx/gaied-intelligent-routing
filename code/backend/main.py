import os
import shutil
import email
from email import policy
import extract_msg
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from document_extractor import DocumentExtractor
from retriever import Retriever
from classifier import Classifier
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Allow Angular frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

retriever = Retriever()
classifier = Classifier()

retriever.add_document("I need a credit card limit increase.", "Credit Card", "Limit Increase")
retriever.add_document("I want to change my bank account details.", "Account Update", "Change Bank Details")

class EmailRequest(BaseModel):
    subject: str
    body: str

def extract_email_content(file_path: str, file_type: str):
    subject, body = "", ""
    
    if file_type == "eml":
        with open(file_path, "rb") as f:
            msg = email.message_from_binary_file(f, policy=policy.default)
            subject = msg["subject"] or "No Subject"
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode(part.get_content_charset(), errors="ignore")
                        break
            else:
                body = msg.get_payload(decode=True).decode(msg.get_content_charset(), errors="ignore")

    elif file_type == "msg":
        msg = extract_msg.Message(file_path)
        subject = msg.subject or "No Subject"
        body = msg.body or "No Body"

    return subject, body

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    file_extension = file.filename.split(".")[-1].lower()
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if file_extension in ["pdf", "docx", "txt"]:
        extracted_text = DocumentExtractor.extract_text(file_path, file_extension)
    elif file_extension in ["eml", "msg"]:
        subject, body = extract_email_content(file_path, file_extension)
        extracted_text = f"Subject: {subject}\nBody: {body}"
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    retrieved_examples = retriever.retrieve_similar(extracted_text)
    label_options = [ex["type"] for ex in retrieved_examples]
    classification_result = classifier.classify_text(extracted_text, label_options)

    return {
        "filename": file.filename,
        "content": extracted_text,
        "classification": classification_result
    }

@app.post("/classify-email/")
async def classify_email(email: EmailRequest):
    email_text = f"Subject: {email.subject}\nBody: {email.body}"
    retrieved_examples = retriever.retrieve_similar(email_text)
    label_options = [ex["type"] for ex in retrieved_examples]
    classification_result = classifier.classify_text(email_text, label_options)

    return {
        "subject": email.subject,
        "body": email.body,
        "classification": classification_result
    }

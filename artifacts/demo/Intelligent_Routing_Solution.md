
## System Overview
This system classifies emails and documents using AI. It extracts content, categorizes it, 
and returns structured classifications.

## Architecture
1. **Frontend (Angular)**: Upload emails and documents, display classifications.
2. **Backend (FastAPI)**: Handles requests, processes files, calls AI models.
3. **AI Processing Layer**:
   - Extractor (FastAPI) extracts text from files.
   - Classifier (Hugging Face) classifies content.
   - Retriever fetches relevant classification info.
4. **Output**: Returns JSON classification results.

## Technology Stack
- **Frontend**: Angular
- **Backend**: FastAPI (Python)
- **AI Models**: Hugging Face Transformers
- **File Processing**: MIME parsing, PDF/Text extraction

## API Endpoints
1. **POST /upload/email** - Uploads an email for processing.
2. **POST /upload/document** - Uploads a document for classification.
3. **GET /results/{id}** - Retrieves classification results.

## Execution Flow
1. User uploads an email/document.
2. FastAPI extracts text.
3. AI model classifies the content.
4. The system returns structured classification.

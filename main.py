from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is live", "status": "running"}

@app.get("/summarize")
def summarize(text: str):
    words = text.strip().split()
    word_count = len(words)
    first_sentence = text.strip().split(".")[0]
    
    return {
        "original_length": word_count,
        "summary": first_sentence,
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root GET route (browser la open panna working message kaatum)
@app.get("/")
def home():
    return {"message": "Titanic Chatbot Backend is Running 🚀"}

# Request model
class ChatRequest(BaseModel):
    message: str

# Chatbot POST route
@app.post("/chat")
def chat(data: ChatRequest):
    user_msg = data.message.lower()

    if "hi" in user_msg:
        return {"response": "Hello 👋 How can I help you about Titanic dataset?"}
    elif "survive" in user_msg:
        return {"response": "In the Titanic dataset, around 342 passengers survived."}
    else:
        return {"response": "Please ask something related to Titanic 🚢"}
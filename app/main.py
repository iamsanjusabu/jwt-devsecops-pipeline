from fastapi import FastAPI
from auth.auth import router as user_register_router
from routers.chat import router as chat_router

app = FastAPI()

app.include_router(user_register_router)
app.include_router(chat_router)

# This is the API health check endpoint
# Endpoint: /
@app.get("/")
def home() -> dict:
    return {"status": "active"}

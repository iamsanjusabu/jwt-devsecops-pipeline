from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from schemas.chat_request import ChatRequest
from auth.jwt_utils import verify_token
import ollama
from dotenv import load_dotenv
from os import getenv

load_dotenv()

router = APIRouter(prefix="/chat")

oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth_2_scheme)) -> str:
    username = verify_token(token)

    return username

@router.post("/")
def chat(request: ChatRequest, username: str = Depends(get_current_user)) -> dict[str, str]:
    model_name = getenv("MODEL_NAME")
    response = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": request.message}]
    )

    return {"response": response["message"]["content"]}
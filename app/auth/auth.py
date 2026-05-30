from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import User
from auth.jwt_utils import create_token
import bcrypt


router = APIRouter(prefix="/auth")

# In-memory db because im lazy
user_db: dict[str, bytes] = {}

# Create user
@router.post("/register")
def user_register(user: User):
    if user.username in user_db:
        raise HTTPException(status_code=409, detail="User already exists")
    
    hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt(rounds=12))
    user_db[user.username] = hashed

    return {"message": "User registered successfully"}

# User login
@router.post("/login")
def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username not in user_db:
        # User not found
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if not bcrypt.checkpw(form_data.password.encode(), user_db[form_data.username]):
        # password mismatch
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token: str = create_token(form_data.username)

    return {"access_token": token, "token_type": "bearer"}
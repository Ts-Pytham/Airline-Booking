from anyio import Any
from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from core.security import create_access_token
from user.models import User
from database import db
from fastapi.security import OAuth2PasswordRequestForm
from user.services import authenticate
api_router = APIRouter(tags=['Auth'])

@api_router.post("/login")
def login(db:Session = Depends(db.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = authenticate(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {
        "access_token": create_access_token(sub=user.email),
        "token_type": "Bearer",
    }
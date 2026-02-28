from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import session
import model,schema,utils
from auth_database import get_db
from jose import jwt
from datetime import datetime , timedelta

SECRET_KEY="-gqDXU8vx8bAOis6pmFpMHAz3UrB-Eecb43MnCmQYyk"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_token(data:dict):
    encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
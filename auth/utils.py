from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['argon2'],deprecated="auto")

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_pass(password:str,hashed_pass:str)->bool:
    return pwd_context.verify(password,hashed_pass)

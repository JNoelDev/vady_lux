from passlib.context import CryptContext

pwd_content = CryptContext(schemes="pbkdf2_sha256",deprecated="auto")

def hash_password(password:str) -> str:
    return pwd_content.hash(password)
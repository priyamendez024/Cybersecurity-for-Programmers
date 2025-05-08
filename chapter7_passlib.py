from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(plain):
    return pwd_ctx.hash(plain)

def verify_password(plain, hashed):
    return pwd_ctx.verify(plain, hashed)
from pydantic import BaseModel, EmailStr, constr

class RegisterUser(BaseModel):
    username: constr(strip_whitespace=True, min_length=3, max_length=20, regex=r'^[a-zA-Z0-9_]+$')
    email: EmailStr
    age: int

def register(data: dict):
    user = RegisterUser(**data)
    # safe to proceed with user.username, user.email, user.age
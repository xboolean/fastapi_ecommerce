from fastapi import Body, FastAPI
from app.domain.schemas.users import UserLogin, User
from app.services.jwt_handler import sign_JWT

app = FastAPI()

@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World"}

@app.post("/user/signup", tags=["user"])
def user_signup(user: User = Body()):
    pass

@app.post("/user/signup", tags=["user"])
def user_login(user: UserLogin = Body()):
    pass
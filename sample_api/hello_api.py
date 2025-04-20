
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HelloAPI(BaseModel):
   name : str

@app.get("/hello")
def say_hello():
   return {"message": "Hello, World!"}

@app.post("/greet")
def greet_user(user: HelloAPI):
   return {"message": f"Hello, {user.name}!"}
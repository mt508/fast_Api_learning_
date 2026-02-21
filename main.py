from fastapi import FastAPI
from typing import Optional#for make query optional 
from pydantic import BaseModel
app=FastAPI()


@app.get("/")
def read_root():
    return {"message":"getmsg"}

@app.get("/about/{name}")
def greet(name:str):
    return{"message":f"hey {name}"} #value paramenter 

@app.get("/about-2/{name}")
def greet(name:str,age:int):#query parameter age writen after ?in url 
    return {"message":f"hey{name}and your age is {age}"}

@app.get("/home-1/{name}")
def home(name:str,age:Optional[int]=None):#optional make the age optional we can give or not its on us 
    return {"message":f"hey{name}and your age is {age}"}

@app.get("/about")
def about(name:str,age:int):#now name and age both became query parameter 
    return {"message":f"hey{name} and your age is {age}"}

class Student(BaseModel):
    name:str
    age:int
    rollno:int
@app.post("/student")
def post_student(student:Student):
    return{
       "name": student.name,
        "age" :student.age,
        "rollno":student.rollno
       
    }
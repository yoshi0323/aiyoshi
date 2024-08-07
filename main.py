from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    body: str

posts = []

@app.get("/posts")
def get_posts():
    return posts

@app.post("/posts")
def create_post(post: Post):
    posts.append(post)
    return post

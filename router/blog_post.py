from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: bool
@router.post("/new")
def create_blog(blog: BlogModel):
    return {"data": blog}
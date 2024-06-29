from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import List, Optional, Dict

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class Image(BaseModel):
    url: str
    alias: str
class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: bool
    tags: List[str] = []
    metadata: Dict[str, str] = {"key: " "val1"}
    image: Optional[Image] = None
@router.post("/new{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version
        }

@router.post("/new/{id}/comment/{comment_id}")
def create_comment(blog: BlogModel, id: int, comment_title: int = Query(None, title="title of the comment", description="Some description for comment_title",
                                                                                  alias="commentTitle",
                                                                                  deprecated=True),
                                                                                  content: str = Body(Ellipsis,
                                                                                                      min_length=10,
                                                                                                      max_length=50,
                                                                                                      regex="^[A-Za-z0-9_]+$"),
                   v: Optional[List[str]] = Query(["1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1"]),
                   comment_id: Optional[int] = Path(gt=5, le=10)
                   ):
    return {
    "blog": blog,
    "id": id,
    "comment_title": comment_title,
    "content": content,
    "version": v,
    "comment_id": comment_id

}

def requires_functionality():
    return {"message": "learning FastAPI is important"}
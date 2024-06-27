from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: bool
@router.post("/new{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version
        }

@router.post("/new/{id}/comment")
def create_comment(blog: BlogModel, id: int, comment_id: int = Query(None, title="id of the comment", description="Some description for comment",
                                                                                  alias="commentId",
                                                                                  deprecated=True),
                                                                                  content: str = Body(Ellipsis,
                                                                                                      min_length=10,
                                                                                                      max_length=50,
                                                                                                      regex="^[A-Za-z0-9_]+$"),
                   v: Optional[List[str]] = Query(["1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1"])

                   ):
    return {
    "blog": blog,
    "id": id,
    "comment_id": comment_id,
    "content": content,
    "version": v

}
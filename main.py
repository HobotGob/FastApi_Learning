from fastapi import FastAPI, status, Response
from enum import StrEnum
from typing import Optional

app = FastAPI()

@app.get("/hello")
def home():
    return {"message": "Hey I am learning this shit"}

#@app.get("/blog/all")
#def get_all_blogs():
    #return {"message": "All Blogs found"}

@app.get("/blog/all",
         tags=["blog"],
         summary="Retrieve all blogs",
         description="This api allows you to retrieve all blogs. "
         )
def get_all_blogs(page = 1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}

@app.get("/blog/{id}/comments/{comment_id}", tags=["blog", "comment"])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulate retrieving comments of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {"message": f"blog {id}, comment_id {comment_id}, valid {valid}, username {username}"}



class BlogType(StrEnum):
    short = "short"
    story = "story"
    howto = "howto"

@app.get("/blog/type/{type}", tags=["blog"])
def get_blog_type(type: BlogType):
    """
    Simulate BlogType retrieval
    - **type** Just you BlogType
    """
    return {"message": f"Blog Type is {type}"}

@app.get("/blog/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error" f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}


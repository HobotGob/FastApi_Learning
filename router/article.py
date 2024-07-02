from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import db_user
from schemas import ArticleBase, ArticleDisplay
from db.database import get_db
from typing import List
from db import db_article

router = APIRouter(
    prefix="/article",
    tags=["article"]
)

@router.post("/", response_model=ArticleBase)
def create_article(request: ArticleBase, db: Session =Depends(get_db)):
    return db_article.create_article(db, request)

@router.get("/{id}", response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article_by_id(db, id)
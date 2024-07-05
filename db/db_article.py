from sqlalchemy.orm import Session
from db.models import DbArticle
from schemas import ArticleBase
from fastapi import HTTPException, status
from exeptions import StoryException

def create_article(db: Session, request: ArticleBase):
    if request.content.startswith("Once upon a time"):
        raise StoryException("No stories please!")
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id

    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_article_by_id(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first
    # Handle errors
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article with id {id} does not exist")
    return article
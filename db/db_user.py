from sqlalchemy.orm import Session
from schemas import UserBase
from db.models import Dbuser
from db.hash import Hash

def create_user(db: Session, request: UserBase):
    new_user = Dbuser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(Dbuser).all()

def get_user(db: Session, id: int):
    return db.query(Dbuser).filter(Dbuser.id == id).first()

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(Dbuser).filter(Dbuser.id == id)
    user.update({
        Dbuser.username: request.username,
        Dbuser.email: request.email,
        Dbuser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return "Okaly"

def delete_user(db: Session, id: int):
    user = db.query(Dbuser).filter(Dbuser.id == id).first()
    db.delete(user)
    db.commit()
    return "Okay"
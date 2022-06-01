from .base import BaseRepository
from sqlalchemy.orm import Session
from app.db.db_setup import get_db
from app.domain.schemas.model import User
from app.domain.schemas.users import UserCreate

class UsersRepository(BaseRepository):
    def get_user_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_users(db: Session, skip: int=0, limit: int=100):
        return db.query(User).offset(skip).limit(limit).all()
    
    def create_user(db: Session, user: UserCreate):
        db_user = User(email=user.email, first_name=user.first_name, last_name=user.last_name, password=user.password, role=user.role)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
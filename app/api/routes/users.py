from fastapi import APIRouter, Depends, Body, HTTPException
from app.db.db_setup import get_db
from app.domain.schemas.users import User
from sqlalchemy.orm import Session
from app.repositories.users import UsersRepository
from app.api.dependencies.database import get_repository

router = APIRouter()

@router.get("/users", response_model=list[User])
async def retrieve_users(db: Session = Depends(get_db), repo: User = Depends(get_repository)):
    pass
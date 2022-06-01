from sqlalchemy import create_engine
from app.domain.schemas.model import Product, ProductUnit, Brand, Category, Media, Order
from sqlalchemy.orm import registry, sessionmaker, selectinload
from config import get_settings
from sqlalchemy import select
from app.db.models.users import mapper_registry 
from app.domain.schemas.model import User

engine = create_engine(get_settings().db_url, echo=True, future=True)

#factory for new session objects
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)



#Db_utility
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

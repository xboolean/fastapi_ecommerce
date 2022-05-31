from sqlalchemy import create_engine
from app.domain.schemas.model import Product, ProductUnit, Brand, Category, Media
from sqlalchemy.orm import sessionmaker, selectinload
from config import get_settings
from app.db.models.catalog import mapper_registry 
from sqlalchemy import select

engine = create_engine(get_settings().db_url, echo=True, future=True)

#factory for new session objects
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = Session()

# with Session.begin() as session:
for row in session.execute(select(Product).options(selectinload(Product.product_units))).scalars():
    print(row.product_units)
    
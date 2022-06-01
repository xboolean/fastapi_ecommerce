from app.domain.schemas.model import User
from app.domain.schemas.model import Order
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Boolean, SmallInteger, Enum
from sqlalchemy.orm import relationship, backref
from app.db.models.catalog import mapper_registry
import enum

class Role(enum.IntEnum):
    manager = 1
    customer = 2

user_table = Table(
        "users",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("email", String(70), unique=True, nullable=False),
        Column("first_name", String(50)),
        Column("last_name", String(50)),
        Column("password", String(150)),
        Column("role", Enum(Role)),
        Column("is_active", Boolean, default=False),
    )

customer_orders = Table(
    "customer_orders",
    mapper_registry.metadata,
    Column("customer_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
)

mapper_registry.map_imperatively(User, user_table, properties={"order": relationship(Order, secondary=customer_orders, backref="user")})
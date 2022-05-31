from dataclasses import dataclass, field
from unicodedata import category
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Boolean, SmallInteger
from sqlalchemy.orm import registry, relationship
from app.domain.schemas import model

mapper_registry = registry()

product_table = Table(
        "product",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name", String(70)),
        Column("slug", String(70)),
        Column("description", String(250)),
        Column("brand_id", Integer, ForeignKey("brand.id")),
        Column("category_id", Integer, ForeignKey("category.id")),
        Column("is_active", Boolean)
    )

product_unit_table = Table(
        "product_unit",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("product_id", Integer, ForeignKey("product.id")),
        Column("sku", String(6)),
        Column("sale_price", Integer),
        Column("store_price", Integer),
        Column("is_active", Boolean)
    )

# product_on_order_table = Table(
#         "products_on_order",
#         mapper_registry.metadata,
#         Column("product_id", ForeignKey("product_units.id")),
#         Column("order_id", ForeignKey("order.id")),
# )

# in_stock_table = Table(
#         "in_stock",
#         mapper_registry.metadata,
#         Column("id", Integer, primary_key=True, autoincrement=True),
#         Column("product", Integer, primary_key=True, autoincrement=True),
#         Column("units_remain", SmallInteger),
#         Column("units_sold", SmallInteger),
#     )

media_table = Table(
        "product_media",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("product_id", Integer, ForeignKey("product_unit.id")),
        Column("img_url", String(200)),
        Column("alt_text", String(100))
    )

category_table = Table(
        "category",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("category", String(50))
    )

brand_table = Table(
        "brand",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("brand", String(50))
    )


mapper_registry.map_imperatively(model.Product, product_table, properties ={'product_units': relationship(model.ProductUnit, backref='product')})

mapper_registry.map_imperatively(model.ProductUnit, product_unit_table)

mapper_registry.map_imperatively(model.Brand, brand_table, properties={"products": relationship(model.Product, backref="brand")})

mapper_registry.map_imperatively(model.Category, category_table, properties={"products": relationship(model.Product, backref="category")})

mapper_registry.map_imperatively(model.Media, media_table, properties={"products": relationship(model.ProductUnit, backref="media")})

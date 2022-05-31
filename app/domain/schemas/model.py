from dataclasses import dataclass
from itertools import product

@dataclass
class Product:
    name: str
    slug: str
    description: str
    brand_id: str
    category_id: str
    is_active: bool

@dataclass
class ProductUnit:
    sku: str
    product_id: int
    # orderid: str
    sale_price: str
    store_price: bool
    is_active: bool

@dataclass
class InStock:
    product_unit_id: int
    units_remain: int
    units_sold: int

@dataclass
class Brand:
    name: str

@dataclass
class Category:
    name: str

@dataclass
class Media:
    product_id: int
    img_url: str
    alt_text: str

@dataclass
class Order:
    pass



from dataclasses import dataclass

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



from pydantic import BaseModel
from typing import List 

class Product(BaseModel):
    product_name : str
    price : str
    rating : str
    seller : str

class ProductList(BaseModel):
    products : List[Product]
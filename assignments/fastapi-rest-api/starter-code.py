from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str
    description: str = ""
    price: float = Field(gt=0)


class Product(ProductCreate):
    id: int


app = FastAPI(title="Product Catalog API")

products: dict[int, Product] = {
    1: Product(id=1, name="Notebook", description="A5 ruled notebook", price=4.5),
    2: Product(id=2, name="Pen", description="Blue ink pen", price=1.25),
}

# Add your GET, POST, PUT, and DELETE routes below.
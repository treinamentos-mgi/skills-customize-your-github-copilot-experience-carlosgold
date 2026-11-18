from fastapi import FastAPI, HTTPException, Response, status
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


@app.get("/products", response_model=list[Product])
def list_products() -> list[Product]:
    return list(products.values())


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int) -> Product:
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate) -> Product:
    product_id = max(products, default=0) + 1
    product = Product(id=product_id, **product_data.dict())
    products[product_id] = product
    return product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product_data: ProductCreate) -> Product:
    if product_id not in products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    product = Product(id=product_id, **product_data.dict())
    products[product_id] = product
    return product


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int) -> Response:
    if product_id not in products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    del products[product_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
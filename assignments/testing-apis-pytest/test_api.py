import pytest
from fastapi.testclient import TestClient

from app import app, products


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_products():
    initial_products = products.copy()
    yield
    products.clear()
    products.update(initial_products)


def test_list_products_returns_seeded_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == "Notebook"


def test_get_existing_product_returns_details():
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Notebook"
    assert response.json()["price"] == 4.5
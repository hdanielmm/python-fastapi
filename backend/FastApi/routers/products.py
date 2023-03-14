from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"message": "Not found"}})

class Product(BaseModel):
    id: int
    name: str

product_list = [
    Product(id=1, name="tv"),
    Product(id=2, name="radio"),
    Product(id=3, name="pc")
]

@router.get("/")
async def products():
    return product_list

@router.get("/{id}")
async def products(id):
    return product_list[id]
from pydantic import BaseModel

class InventoryResponse(BaseModel):
    warehouse_id: int
    product_id: int
    stock: int

    class Config:
        from_attributes = True
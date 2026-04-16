from pydantic import BaseModel, Field

class OrderCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    location: str
    priority: str = Field(pattern="^(fast|cheap|balanced)$")
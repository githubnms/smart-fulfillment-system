from fastapi import FastAPI

app = FastAPI(
    title="Smart Fulfillment System",
    description="""
    A distributed system for order fulfillment and delivery optimization.

    Features:
    - Inventory Allocation Engine
    - Delivery Optimization Engine
    - Simulation of high-scale orders
    - AWS-based deployment
    """,
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Smart Fulfillment System API is running 🚀",
        "status": "healthy"
    }
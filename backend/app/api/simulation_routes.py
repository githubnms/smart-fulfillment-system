from fastapi import APIRouter
from app.services.simulation_service import run_simulation

router = APIRouter()

@router.get("/run-simulation")
def simulate():
    return run_simulation()
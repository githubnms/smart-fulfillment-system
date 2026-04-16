from fastapi import FastAPI
from app.db.database import engine

app = FastAPI()

@app.on_event("startup")
def test_db_connection():
    try:
        with engine.connect() as connection:
            print("Database connected successfully!")
    except Exception as e:
        print("Database connection failed:", e)

@app.get("/")
def read_root():
    return {"message": "API + DB Ready 🚀"}
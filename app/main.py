from fastapi import FastAPI
from app.routers import items
from app.database import engine, Base

app = FastAPI()

# Crea todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(items.router)
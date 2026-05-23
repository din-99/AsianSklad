from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import products, users

# Создаём таблицы, если их ещё нет
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AsianSklad API")

# CORS (разрешаем запросы от фронтенда)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(products.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "AsianSklad API is running"}
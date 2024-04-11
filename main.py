import os

from databases import Database
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from django.core.mail import send_mail
from django.contrib.auth.models import User

from config import settings

# # Создаем экземпляр FastAPI приложения
# app = FastAPI()
#
# # Определяем маршрут "/"
# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


app = FastAPI()

database = Database(settings.DATABASES['default'])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

class Document(BaseModel):
    name: str

@app.post("/upload_document/")
async def upload_document(document: Document):
    # Обработка загруженного документа
    # Отправка уведомления администратору
    send_mail('Новый документ', 'Поступил новый документ', 'from@example.com', ['admin@example.com'])

    return JSONResponse(content=jsonable_encoder({"message": "Документ успешно загружен"}))

@app.post("/create_superuser/")
async def create_superuser():
    # Создание суперпользователя
    user = User.objects.create(
        email='from@example.com',
        username='Admin',
        is_staff=True,
        is_superuser=True,
        is_active=True
    )
    user.set_password(os.getenv('ADMIN_PASSWORD'))
    user.save()

    return JSONResponse(content=jsonable_encoder({"message": "Суперпользователь успешно создан"}))
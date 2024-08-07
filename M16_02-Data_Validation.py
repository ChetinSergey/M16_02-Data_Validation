from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get("/")
async def home_page() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def user_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def users_id(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}!"


@app.get("/user")
async def users_name(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age} лет."


@app.get("/user/{username}/{age}")
async def enter_user_id(username: Annotated[str, Path(min_length=5, max_length=20,
                                                      description="Введите Ваш номер", example="ChetinSergey")]
                        , age: Annotated[int, Path(ge=18, le=120, description="Введите возраст", example=38)]) -> str:
    return f"Пользователь: {username}, Возраст: {age}"

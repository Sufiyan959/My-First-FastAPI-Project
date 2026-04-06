from fastapi import FastAPI
from src.utils.settings import settings
from src.utils.db import get_db, Base, engine
from src.tasks.model import TaskModel
from src.tasks.router import tasks_router
from src.user.router import user_router

Base.metadata.create_all(engine)


app = FastAPI()

app.include_router(tasks_router)
app.include_router(user_router)

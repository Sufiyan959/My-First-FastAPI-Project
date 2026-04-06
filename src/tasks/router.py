from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from typing import List
from src.utils.helper import is_authenticated
from src.user.model import UserModel

tasks_router = APIRouter(prefix="/tasks")


@tasks_router.post(
    "/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED
)
def create_task(
    body: TaskSchema, db=Depends(get_db), user: UserModel = Depends(is_authenticated)
):
    return controller.create_task(body, db, user)


@tasks_router.get(
    "/all_tasks",
    response_model=List[TaskResponseSchema],
    status_code=status.HTTP_200_OK,
)
def get_tasks(db=Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.get_tasks(db, user)


@tasks_router.get(
    "/one_task/{task_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_200_OK,
)
def get_one_task(
    task_id: int, db=Depends(get_db), user: UserModel = Depends(is_authenticated)
):
    return controller.get_one_task(task_id, db)


@tasks_router.put(
    "/update_task/{task_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_200_OK,
)
def update_task(
    task_id: int,
    body: TaskSchema,
    db=Depends(get_db),
    user: UserModel = Depends(is_authenticated),
):
    return controller.update_task(task_id, body, db, user)


@tasks_router.delete(
    "/delete_task/{task_id}",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    task_id: int, db=Depends(get_db), user: UserModel = Depends(is_authenticated)
):
    return controller.delete_task(task_id, db, user)

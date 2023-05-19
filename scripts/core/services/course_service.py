from fastapi import APIRouter
from schemas.models import Student
from scripts.core.handlers.course_handler import get_course, add_course, update_course, delete_course, pipe_line
from scripts.constants.app_constants import API
from scripts.core.handlers.email_handlers import Email, send_email

app_router = APIRouter()


@app_router.get(API.view_course)
def func(course_name: str):
    try:
        return get_course(course_name)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(API.add_course)
def func(sid: Student):
    try:
        return add_course(sid)
    except Exception as e:
        return {"Error": str(e)}


@app_router.put(API.update_course)
def func(course_name: str, new_course: Student):
    try:
        return update_course(course_name, new_course)
    except Exception as e:
        return {"Error": str(e)}


@app_router.delete(API.delete_course)
def func(course_name: str):
    try:
        return delete_course(course_name)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(API.send_email)
def func(email: Email):
    try:
        Total_price = pipe_line()
        return send_email(str(Total_price), email)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get(API.Total_price)
def func():
    return pipe_line()

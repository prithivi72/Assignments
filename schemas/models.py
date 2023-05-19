from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    course: str
    course_price: float
    dept: str


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str

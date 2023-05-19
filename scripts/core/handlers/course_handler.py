import logging
from schemas.models import Student
from scripts.core.db.mongo_db import collection


def get_course(course: str):
    try:
        dept = collection.find_one({"course": course})
        if dept:
            return {"course is available"}
        return {"Error": "course not found"}
    except Exception as e:
        return {"Error": str(e)}


def add_course(sid: Student):
    try:

        result = collection.insert_one(sid.__dict__)
        return {"Message": "course added successfully", "Status": "Success"}
    except Exception as e:
        return {"Error": str(e)}


def update_course(course_name: str, student):
    try:
        response = collection.update_one({"course": course_name}, {"$set": student.__dict__})
        if response.modified_count > 0:
            return {"message": "Course updated successfully", "Status": "Success"}
        return {"Error": "Course not found", "Status": "Failed"}
    except Exception as a:
        return {"Error": str(a)}


def delete_course(course_name: str):
    try:
        response = collection.delete_one({"course": course_name})
        if response.deleted_count > 0:
            return {"Message": "Course deleted successfully", "Status": "Success"}
        return {"Error": "course not found", "Status": "Failed"}
    except Exception as a:
        return {"Error": str(a)}


def pipe_line():
    pipe_agg = [
        {
            '$group': {
                '_id': None,
                'Total_price': {
                    '$sum': '$price'
                }
            }
        }, {
            '$project': {
                '_id': 0
            }
        }
    ]
    data = collection.aggregate(pipe_agg)
    data = list(data)
    logging.info(data)
    return {"Total_Price": data[0]['Total_price']}

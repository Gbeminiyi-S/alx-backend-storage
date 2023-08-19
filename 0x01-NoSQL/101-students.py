#!/usr/bin/env python3
"""This modules defines a function `top_students`"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    mapped_students = mongo_collection.aggregate([
        {
            "$project": {
                "_id": "$_id",
                "name": "$name",
                "averageScore": {"$avg": "$topis.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ])

    return mapped_students

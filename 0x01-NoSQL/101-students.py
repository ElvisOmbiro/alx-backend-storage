#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July  17 23:50:00 2024

@Author: Elvis Ombiro
"""


def top_students(mongo_collection):
    """Returns the top 10 students with the highest average score.

    Args:
        mongo_collection (Collection): pymongo collection.

    Returns:
        List[dict]: top 10 students with the highest average score.
    """
    students = list(mongo_collection.find())

    for student in students:
        scores = [topic["score"] for topic in student["topics"]]
        average_score = sum(scores) / len(scores)
        student["averageScore"] = average_score

    sorted_students = sorted(
            students,
            key=lambda x: x["averageScore"],
            reverse=True)
    return sorted_students

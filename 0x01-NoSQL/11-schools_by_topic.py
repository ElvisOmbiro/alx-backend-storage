#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July  17 23:47:00 2024

@Author: Elvis Ombiro
"""


def schools_by_topic(mongo_collection, topic: str):
    """
    Returns a list of schools that have a certain topic.

    Args:
        mongo_collection (Collection): A pymongo collection.
        topic (str): The topic to search for.

    Returns:
        List[str]: A list of schools that have a certain topic.
    """
    return list(mongo_collection.find({"topics": topic}))

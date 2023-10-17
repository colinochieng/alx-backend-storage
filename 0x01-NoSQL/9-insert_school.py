#!/usr/bin/env python3
'''
Module for practicing pymongo insertion
'''


def insert_school(mongo_collection, **kwargs):
    '''
    description: function that inserts a new
        document in a collection based on kwargs
    args:
        mongo_collection: mongodb collection instance
        kwargs: dict of data to insert
    return: new _id
    '''
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id

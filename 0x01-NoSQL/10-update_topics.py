#!/usr/bin/env python3
'''
Module for updating a mongodb collection document
'''


def update_topics(mongo_collection, name, topics):
    '''
    description:  function that changes all topics of a
        school document based on the name
    Args:
        mongo_collection: mongodb collection
        name: name of document
             (string) will be the school name to update
        topics: (list of strings) will be the
            list of topics approached in the school
    return: None
    '''
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
            )

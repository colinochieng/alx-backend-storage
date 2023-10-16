#!/usr/bin/env python3
'''
Module for querying and filtering
info from mongodb
'''


def schools_by_topic(mongo_collection, topic):
    '''
    description: function that returns the
        list of school having a specific topic
    Args:
        mongo_collection: the pymongo collection object
        topic: (string) will be topic searched
    return: list of schools
    '''
    return list(mongo_collection.find({'topics': topic}))

#!/usr/bin/env python3
'''
Module for startup of PyMongo
'''


def list_all(mongo_collection):
    '''
    description: lists all documents in a mongodb collection
    mongo_collection: mongodb collection to use
    return: list of collection
    '''
    return list(mongo_collection.find({}))

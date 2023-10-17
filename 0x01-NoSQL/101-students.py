#!/usr/bin/env python3
'''
Module for sorting in pymongo
'''


def top_students(mongo_collection):
    '''
    description: function that returns all
        students sorted by average score
    Args:
        mongo_collection: pymongo collection object
    Return: all students sorted by average score
    '''
    pipeline = [
            {'$unwind': '$topics'},
            {
                '$group': {
                    '_id': '$_id',
                    'name': {'$first': '$name'},
                    'averageScore': {'$avg': '$topics.score'}
                    }
                },
            {'$sort': {'averageScore': -1}}
            ]

    return list(mongo_collection.aggregate(pipeline))

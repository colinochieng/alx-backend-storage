#!/usr/bin/env python3
'''
Module traversing data
Script provides some stats about Nginx logs stored in MongoDB:
'''

if __name__ == '__main__':
    import pymongo

    client = pymongo.MongoClient('mongodb://localhost:27017')

    nginx_col = client.logs.nginx

    # displaying number of logs
    print(f'{len(list(nginx_col.find()))} logs')

    print('Methods:')

    pipe = [
            {'$group': {'_id': '$method', 'count': {"$sum": 1}}}
            ]
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    result = list(nginx_col.aggregate(pipe))

    for data in result:
        if data['_id'] in methods:
            print(f'\tmethod {data["_id"]}: {data["count"]}')

            methods.remove(data['_id'])

    for method in methods:
        print(f'\tmethod {method}: 0')

    print(f'{len(list(nginx_col.find({"path": "/status"})))} status check')

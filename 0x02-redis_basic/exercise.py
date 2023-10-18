#!/usr/bin/env bash
'''
Module implementing data storage using
Redis key-value NoSQL
'''
from typing import Callable, Optional, TypeVar, Union
import redis
import uuid
from functools import wraps

T = TypeVar('T')


def count_calls(method: Callable[[], None]) -> Callable[[], None]:
    '''
    description: count the number of calls to the Cache
    method: wrapped function
    Returns: Callable
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        desc: wrapper function
        Args:
            args: variable arguments
            kwargs: keywords
        '''
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable[[], None]) -> Callable[[], None]:
    '''

    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        desc: wrapper function
        Args:
            args: variable arguments
            kwargs: keywords
        '''
        method_name = method.__qualname__
        inputs_key = method_name + ":inputs"
        outputs_key = method_name + ":outputs"

        input_str = str(args)
        self._redis.rpush(inputs_key, input_str)

        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(output))

    return output


class Cache():
    '''
    description: Blueprint for an instance of Redis client
    attributes:
        _redis: private varibale, redis client
            flushed after instantiating
    '''
    def __init__(self):
        '''
        instantiating method
        '''
        self._redis: redis.Redis = redis.Redis()

        # flushing the instance the instance
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, int, bytes, float]) -> str:
        '''
        description: generates a random uuid key and use it
            to store the data object in redis client
        Args:
            data: value to store in redis
                stored under key (UUID string)
        Return: key used to store the value (UUID string)
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None) -> T:
        '''
        description: function to retrive data based on key
        Args:
            key: key to search for
            fn: function to convert data to the desired data type
        Return: value returned by fn or None if the key is invalid
        '''
        value = self._redis.get(key)

        try:
            return fn(value) if value else value
        except Exception as e:
            return value

    def get_str(self, key: str) -> Union[str, None]:
        '''
        description: gets a string value from db
        Args:
            key: key to search for
        Return: string value or None
        '''

        def decoder(value: bytes) -> str:
            '''
            value: data from Redis db
            '''
            return value.decode('utf-8')

        return self.get(key, decoder)

    def get_int(self, key: str) -> Union[int, None]:
        '''
        description: gets a integer value from db
        Args:
            key: key to search for
        Return: integer value or None
        '''
        return self.get(key, int)

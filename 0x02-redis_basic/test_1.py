from exercise import Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    # print(f'get: {cache.get(key, fn=fn)} == value: {value}')
    assert cache.get(key, fn=fn) == value

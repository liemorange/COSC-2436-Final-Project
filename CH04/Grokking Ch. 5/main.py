class Cache:
    def __init__(self, size):
        self.size = size
        self.cache = {}
    def put(self, key, value):
        self.cache[key] = value
    def get(self, key):
        return self.cache.get(key, "Not Found")

import redis


class RedisClient:
    instance = None
    host = "127.0.0.1"
    port = 6379

    def __init__(self):
        self.instance = redis.Redis(host=self.host, port=self.port, db=0)

    def get(self, key):
        return str(self.instance.get(key), "utf-8")

    def set(self, key, value):
        return self.instance.set(name=key, value=value)

    def incrby(self, key, add):
        return self.instance.incrby(name=key, amount=add)
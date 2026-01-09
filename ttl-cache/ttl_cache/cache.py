from cachetools import TTLCache

from .parser import StockTradeRequest

class Cache:

    def __init__(self):
        self.cache = TTLCache(maxsize=100_00, ttl=60)

    def is_dup(self, id) -> bool:
        return id in self.cache

    def add(self, item, id) -> None:
        self.cache[id] = item

import time

from ttl_cache.cache import Cache
from ttl_cache.parser import StockTradeRequest, Operation

def test_cache():
    cache = Cache(5)
    current_time = int(time.time())
    request_a = StockTradeRequest("aapl", "kymry", current_time, Operation.BUY, 1)
    request_b = StockTradeRequest("aapl", "kymry", current_time, Operation.BUY, 1)
    cache.add(request_a)
    cache.add(request_b)

    assert cache.size() == 1

    time.sleep(6)
    assert cache.size() == 0

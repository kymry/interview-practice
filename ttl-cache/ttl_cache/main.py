import asyncio

from ttl_cache.server import TCPServer
from ttl_cache.parser import StockTradeRequest
from ttl_cache.cache import Cache


class Handler:

    def __init__(self):
        self.parser = StockTradeRequest
        self.cache = Cache()

    def handle(self, line: str) -> bool:
        request = self.parser.from_json(line)
        is_dup = self.cache.is_dup(request.dedup_key)
        print(f"Received request: {request}")
        print(f"Is dupe: {is_dup}")
        self.cache.add(request, request.dedup_key)
        print(f"finished caching")
        return is_dup

async def main():
    handler = Handler()
    server = TCPServer(handler=handler, host="0.0.0.0", port=9999)
    await server.start()
    await server.serve_forever()

def run():
    import asyncio
    asyncio.run(main())
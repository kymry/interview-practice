import asyncio

class TCPServer:
    def __init__(self, handler, host="0.0.0.0", port=9999):
        self.host = host
        self.port = port
        self._server = None
        self.handler = handler

    async def handle_client(self, reader, writer):
        addr = writer.get_extra_info("peername")
        print(f"Connected: {addr}")

        async for line in reader:
            print("Received:", line.decode().strip())
            self.handler.handle(line)

        writer.close()
        await writer.wait_closed()

    async def start(self):
        self._server = await asyncio.start_server(
            self.handle_client,
            self.host,
            self.port,
        )
        print(f"Server listening on {self.host}:{self.port}")

    async def serve_forever(self):
        async with self._server:
            await self._server.serve_forever()

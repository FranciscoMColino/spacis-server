import asyncio

import websockets

from spacis_utils import parse_settings
from ws_server import WsServer


async def main():

    settings = parse_settings()

    server = WsServer()

    await server.start()

    while True:
        await asyncio.sleep(1)

asyncio.run(main())

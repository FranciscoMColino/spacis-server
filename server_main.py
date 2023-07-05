import asyncio

import websockets

import ws_server


async def main():

    server = ws_server.WsServer()

    await server.start()

    while True:
        await asyncio.sleep(1)

asyncio.run(main())

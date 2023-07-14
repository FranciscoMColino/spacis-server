import asyncio

import websockets

PORT = 8765
HOST = "100.121.193.123"

async def client():
    server_address = "ws://" + HOST + ":" + str(PORT)
    async with websockets.connect(server_address) as websocket:
        # Send messages to the server
        await websocket.send("Hello, server!")

        # Receive and print the server's response
        response = await websocket.recv()
        print(f"Received response from server: {response}")

# Run the client
asyncio.get_event_loop().run_until_complete(client())

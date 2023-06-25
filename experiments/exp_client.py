import asyncio

import websockets

PORT = 8765
HOST = "16.171.4.184"

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

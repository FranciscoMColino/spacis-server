import asyncio

import websockets

PORT = 8765

async def server(websocket, path):
    # Handle incoming messages from the client
    async for message in websocket:
        print(f"Received message from client: {message}")
        
        # Echo the message back to the client
        await websocket.send(f"Server received: {message}")

# Start the server
start_server = websockets.serve(server, "0.0.0.0", PORT)

# Run the event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

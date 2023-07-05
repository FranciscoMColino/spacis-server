import asyncio

import websockets

PORT = 8765
TAILSCALE_IP =  "100.121.193.123"

async def server(websocket, path):
    # Handle incoming messages from the client
    async for message in websocket:
        print(f"Received message from client: {message}")
        
        # Echo the message back to the client
        await websocket.send(f"Server received: {message}")

# Start the server
start_server = websockets.serve(server, TAILSCALE_IP, PORT)

# Run the event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

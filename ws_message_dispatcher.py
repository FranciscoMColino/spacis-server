import asyncio

ON_DISPATCH_INTERVAL = 1/10
NO_ACTIVITY_INTERVAL = 1

class WsMessageDispatcher:
    def __init__(self, client):
        self.client = client
        self.message_buffer = [] # messages to receive
    
    async def periodic_dispatch(self):
        while True:
            if self.client.connected and self.client.websocket.open:
                if len(self.message_buffer) > 0:
                    await self.client.websocket.send(self.message_buffer.pop(0))
                    await asyncio.sleep(ON_DISPATCH_INTERVAL)
                    continue
            await asyncio.sleep(NO_ACTIVITY_INTERVAL)

    def add_message(self, message):
        self.message_buffer.append(message)

import asyncio

ON_DISPATCH_INTERVAL = 1/100
NO_ACTIVITY_INTERVAL = 1/5

class WsMessageDispatcher:
    def __init__(self, client):
        self.client = client
        self.message_buffer = [] # messages to receive
    
    async def periodic_dispatch(self):
        while True:
            print("LOG: periodic dispatch")
            if self.client.connected and self.client.websocket.open:
                
                if len(self.message_buffer) > 0:
                    message = self.message_buffer.pop(0)
                    print("LOG: dispatching message: {}".format(message))
                    await self.client.websocket.send(message)
                    #await asyncio.sleep(ON_DISPATCH_INTERVAL)
                    continue
            #await asyncio.sleep(NO_ACTIVITY_INTERVAL)

    def add_message(self, message):
        self.message_buffer.append(message)

import asyncio
import json

ON_DISPATCH_INTERVAL = 1/100
NO_ACTIVITY_INTERVAL = 1/5

class WsMessageDispatcher:
    def __init__(self, client):
        self.client = client
        self.message_buffer = [] # messages to receive
    
    async def periodic_dispatch(self):
        while True:
            #print("LOG: periodic dispatch")
            try:
                if self.client.websocket is not None and self.client.websocket.open:
                    
                    if len(self.message_buffer) > 0:
                        message = self.message_buffer.pop(0)
                        print("LOG: dispatching message: {}".format(message.keys()))
                        print("LOG: {} messages in buffer".format(len(self.message_buffer)))
                        await self.client.websocket.send(json.dumps(message))
                        print("LOG: message sent")
                        #await asyncio.sleep(ON_DISPATCH_INTERVAL)
                    else:
                        await asyncio.sleep(NO_ACTIVITY_INTERVAL)
                else:
                    await asyncio.sleep(NO_ACTIVITY_INTERVAL)
                    # print("LOG: WebSocket not connected, {}".format(self.client.websocket.open if self.client.websocket is not None else "None"))
            except Exception as e:
                print("LOG: error dispatching message: {}".format(e))
                await asyncio.sleep(NO_ACTIVITY_INTERVAL)

    def add_message(self, message):
        self.message_buffer.append(message)

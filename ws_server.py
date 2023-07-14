import asyncio
import json

import websockets

import ws_message_dispatcher

WS_PORT = 8765
WS_HOST = '172.31.1.110'

class Client:
    def __init__(self):
        self.connected = False
        self.last_update = ""
        self.websocket = None

class WsServer:
    def __init__(self):
        self.server = None
        self.ss_client = Client()
        self.gcs_client = Client()
        self.ss_msg_dispatch = ws_message_dispatcher.WsMessageDispatcher(self.ss_client)
        #self.gcs_msg_dispatch = ws_message_dispatcher.WsMessageDispatcher(self.gcs_client)
        self.relay_message_types = ["sensor_data", "gps_data"]

    async def start(self):
        self.server = await websockets.serve(self.handler, WS_HOST, WS_PORT)
        print("LOG: Server started")
        asyncio.create_task(self.ss_msg_dispatch.periodic_dispatch())
    
    def received_message_handler(self, message):
        try:
            message = json.loads(message)

            if message["user"] == "ground-control-station":
                content = message["content"]
                if content["type"] in self.relay_message_types:
                    print("RECEIVED: message from ground control station, type {}".format(content["type"]))
                    self.ss_msg_dispatch.add_message(message)
                else:
                    print("RECEIVED: invalid message type from ground control station, type {}".format(content["type"]))
            elif message["user"] == "sound-station":
                print("RECEIVED: message from sound station")
            else:
                print("RECEIVED: invalid user")

        except json.decoder.JSONDecodeError:
            print("RECEIVED: invalid message format (not JSON)")


    async def handler(self, websocket):
        try:
            async for message in websocket:

                # Connection handler

                # TODO better handshake
                if message == 'sound-station-connect' and not self.ss_client.connected:
                    self.ss_client.websocket = websocket
                    self.ss_client.connected = True
                    print('LOG: Sound Station connected')
                elif message == 'sound-station-connect' and self.ss_client.connected:
                    print('LOG: Sound Station already connected')
                elif message == 'ground-control-station-connect' and not self.gcs_client.connected:
                    self.gcs_client.websocket = websocket
                    self.gcs_client.connected = True
                    print('LOG: Ground Control Station connected')
                elif message == 'ground-control-station-connect' and self.gcs_client.connected:
                    print('LOG: Ground Control Station already connected')
                else:
                    self.received_message_handler(message)
        except Exception as e:
            # Handle the exception or log it as needed
            print(f"ERROR: WebSocket connection error: {e}")

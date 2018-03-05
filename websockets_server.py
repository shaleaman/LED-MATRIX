#!/usr/bin/env python

import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))


start_server = websockets.serve(time, '10.0.0.41', 5555)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
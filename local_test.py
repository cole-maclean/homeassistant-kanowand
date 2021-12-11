import asyncio
import time
from kanowandasync import Shop, Wand

async def connect_wand():
    wand_loop = asyncio.new_event_loop()
    w = Wand(device_addr="B6DA9E44-9712-49E3-A451-3E6E2AE859EF",name = "Kano-Wand-2f-44-3d",
             bot_loop=wand_loop)
    await w.connect()
    await w.subscribe_button()


if __name__ == "__main__":
    asyncio.run(connect_wand(), debug=True)
    while True:
        time.sleep(100)
        print("heartbeat")







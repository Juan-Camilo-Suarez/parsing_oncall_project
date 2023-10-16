import os
import time
import asyncio
import logging
from fastapi import FastAPI
from prometheus_client import start_http_server
from endpoints_conecctions import RequesOncall

app = FastAPI()

session_oncall = RequesOncall('root', 'admin')


async def worker():
    while True:
        teams = session_oncall.get_teams()
        # Realiza otras tareas según sea necesario

        # Espera durante el período de rastreo
        await asyncio.sleep(scrape_duration)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    scrape_duration_str = os.getenv("scrape-duration", "30s")
    scrape_duration = int(scrape_duration_str.split('s')[0])
    port = int(os.getenv("port", 9213))
    silent = bool(os.getenv("silent", False))

    start_http_server(port)

    loop = asyncio.get_event_loop()
    loop.create_task(worker())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()

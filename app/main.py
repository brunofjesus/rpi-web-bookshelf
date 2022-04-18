import time
from multiprocessing import Process

import fetch
import web


def spawn_fetch():
    fetch_process = Process(target=fetch.periodic_fetch, args=())
    fetch_process.start()
    return fetch_process


def spawn_web():
    http_server_process = Process(target=web.main, args=())
    http_server_process.start()
    return http_server_process


if __name__ == "__main__":
    fetch = spawn_fetch()
    web = spawn_web()

    while True:
        if not fetch.is_alive():
            spawn_fetch()
        if not web.is_alive():
            spawn_web()

        time.sleep(60)

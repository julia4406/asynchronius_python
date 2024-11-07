import time
import httpx
import threading
from typing import Tuple

Urls = Tuple[str, ...]

urls = ("https://www.google.com",) * 50

def send_request(count: int, url: str, client: httpx.Client):
    print(f"Sending request #{count}")
    response = client.get(url)
    print(f"got response for request {count}, status code: {response.status_code}")


def main_threads(in_urls: Urls = urls):
    with httpx.Client() as client:
        tasks = []
        for count, url in enumerate(in_urls):
            tasks.append(threading.Thread(
                target=send_request,
                args=(count, url, client)
            ))
            tasks[-1].start()

        for task in tasks:
            task.join()


if __name__ == "__main__":
    start = time.perf_counter()
    main_threads(urls)
    threads_duration = time.perf_counter() - start
    print(threads_duration)

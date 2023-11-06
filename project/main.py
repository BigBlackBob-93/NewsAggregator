from threading import Thread
from queue import Queue
from time import (
    sleep,
    time,
)

import keyboard

from project.resources.altair import Altair
from project.resources.aljazeera import Aljazeera
from project.resources.globaltimes import GlobalTimes
from project.resources.globaltimes import News


def scraper(resource: News, queue: Queue) -> None:
    html: str = resource.get_html().text
    for article in resource.get_new_article(html=html):
        queue.put(article)


def update(queue: Queue, resources: tuple) -> None:
    print('UPDATE')
    for resource in resources:
        Thread(
            target=scraper,
            args=(
                resource,
                queue,
            ),
        ).start()


if __name__ == '__main__':
    res: tuple = (
        Altair(),
        GlobalTimes(),
        Aljazeera(),
    )

    q = Queue()

    start = time()
    update(queue=q, resources=res)

    while not keyboard.is_pressed('ctrl + c'):
        if (time() - start) >= 60:
            start = time()
            update(queue=q, resources=res)
        if not q.empty():
            print(q.get().model_dump_json())
            sleep(0.5)

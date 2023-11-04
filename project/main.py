from project.resources.altair import Altair
from project.resources.aljazeera import Aljazeera
from project.resources.globaltimes import GlobalTimes


def crt_html(text: str, name: str) -> None:
    with open(name + '.html', 'w', encoding="utf-8") as f:
        f.write(text)


def get_html(name: str) -> str:
    with open(name + '.html', 'r', encoding="utf-8") as f:
        return f.read()


if __name__ == '__main__':
    altair: Altair = Altair()
    altair.parse_html(
        html=altair.get_html().text,
    )

    aljazeera: Aljazeera = Aljazeera()
    aljazeera.parse_html(
        html=aljazeera.get_html().text,
    )

    global_times: GlobalTimes = GlobalTimes()
    global_times.parse_html(
        html=global_times.get_html().text,
    )

from project.resources.base import (
    News,
    Response,
    Article,
)
from bs4 import BeautifulSoup


class GlobalTimes(News):
    def __init__(self):
        super().__init__(url='https://www.globaltimes.cn/life/index.html')

    def get_html(self) -> Response:
        return super().get_html()

    def parse_html(self, html: str) -> None:
        soup = BeautifulSoup(html, "html.parser")

        for new in soup.findAll('div', class_='list_info'):
            header: str = new.find('a', class_='new_title_ms').text

            if self.history.is_unique(header=header):
                self.history.upd(header=header)

                other: list[str] = new.find(
                    'div',
                    class_='source_time',
                ).text.split('|')

                article: Article = Article(
                    header=header,
                    annotation=new.find('p').text,
                    author=other[0].replace('By ', ''),
                    date=other[1].split(' ')[2],
                )

                print(f'Resource - {self.__class__.__name__}:{article}')

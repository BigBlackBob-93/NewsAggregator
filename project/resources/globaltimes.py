from bs4 import BeautifulSoup

from project.resources.base import (
    News,
    Article,
)


class GlobalTimes(News):
    def __init__(self):
        super().__init__(url='https://www.globaltimes.cn/life/index.html')

    def get_new_article(self, html: str) -> Article | None:
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

                yield article

from project.resources.base import (
    News,
    Response,
    Article,
)
from bs4 import BeautifulSoup


class Aljazeera(News):
    def __init__(self):
        super().__init__(url='https://www.aljazeera.com/middle-east/')

    def get_html(self) -> Response:
        return super().get_html()

    def parse_html(self, html: str) -> None:
        soup = BeautifulSoup(html, "html.parser")

        for new in soup.find(id="news-feed-container").find_all('article'):
            header: str = new.find('h3', class_='gc__title').find('span').text.replace('\xad', '')

            if self.history.is_unique(header=header):
                self.history.upd(header=header)

                article: Article = Article(
                    header=header,
                    annotation=new.find('div', class_='gc__excerpt').find('p').text.replace('\xad', ''),
                    date=new.find('div', class_='gc__date__date').find('span').text.replace('Published On ', ''),
                )

                print(f'Resource - {self.__class__.__name__}:{article}')

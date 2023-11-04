from project.resources.base import (
    News,
    Response,
    Article,
)
from bs4 import (
    BeautifulSoup,
    Tag,
)


class Altair(News):
    def __init__(self):
        super().__init__(url='https://www.altair.com.pl/')

    def get_html(self) -> Response:
        return super().get_html()

    def parse_html(self, html: str) -> None:
        soup = BeautifulSoup(html, "html.parser")

        main: Tag = soup.find('div', class_='colMain')
        dates: list[Tag] = main.find_all('h4', class_='redHead')

        for index, block in enumerate(
                main.find_all(
                    'ul',
                    class_='leads',
                )
        ):
            for new in block.find_all('li'):
                header: str = new.find('h3', class_='smallCaps').find('a').text.replace('\xa0', ' ')

                if self.history.is_unique(header=header):
                    self.history.upd(header=header)

                    article: Article = Article(
                        header=header,
                        annotation=new.find('p').text.replace('\xa0', ' ').replace(' czytaj więcej', ''),
                        date=dates[index].text.replace('\xa0', ' '),
                    )

                    print(f'Resource - {self.__class__.__name__}:{article}')

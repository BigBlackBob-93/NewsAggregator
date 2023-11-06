from abc import (
    ABC,
    abstractmethod,
)

from pydantic import BaseModel
from requests import (
    get,
    Response,
)


class Article(BaseModel):
    header: str
    annotation: str
    author: str = 'John Doe'
    date: str | None = None


class History:
    def __init__(self):
        self.registry: list[str] | None = None

    def upd(self, header: str) -> None:
        if self.registry is None:
            self.registry = [header]
        else:
            self.registry.append(header)

    def is_unique(self, header: str) -> bool:
        if self.registry is not None:
            return not (header in self.registry)
        return True


class News(ABC):

    def __init__(self, url: str):
        self.url: str = url
        self.history: History = History()

    def get_html(self) -> Response:
        return get(url=self.url)

    @abstractmethod
    def get_new_article(self, html: str) -> Article | None:
        pass

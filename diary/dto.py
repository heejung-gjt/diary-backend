from dataclasses import dataclass
import time


@dataclass
class ArticleCreateDto():
    title : str
    content : str
    file : str


@dataclass
class ArticleIdDto():
    id : int


@dataclass
class ArticleUpdateDto():
    id : int
    title : str
    content : str
    file: str
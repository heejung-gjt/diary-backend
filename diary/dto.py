from dataclasses import dataclass


@dataclass
class ArticleCreateDto():
    title : str
    content : str
    file : str
    user_pk : int


@dataclass
class ArticleIdDto():
    id : int
    user_pk: int


@dataclass
class ArticleUpdateDto():
    id : int
    title : str
    content : str
    file: str

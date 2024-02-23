from typing import Optional


class BaseAppException(Exception):
    title: str = 'Error'
    content: Optional[str] = None
    desc: Optional[str] = None

    def __init__(
            self,
            title: Optional[str] = None,
            content: Optional[str] = None,
            desc: Optional[str] = None
    ):
        self.title = title or self.title
        self.content = content or self.content
        self.desc = desc or self.desc

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}(title={self.title!r}, content={self.content!r}, desc={self.desc})'

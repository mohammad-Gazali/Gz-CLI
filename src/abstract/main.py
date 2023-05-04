from typing import List, Dict
from abc import ABC, abstractstaticmethod, abstractclassmethod



class CDNProvider:
    name: str
    provider_endpoint: str


class CDNPackage:
    name: str
    cdn_provider: CDNProvider
    need_tailwind: bool
    paths: List[Dict[str, str]]

    @classmethod
    def cdn_url(cls):
        return f"{cls.cdn_provider.provider_endpoint}/{cls.name}"

    @classmethod
    def get_full_name(cls):
        return f"{cls.name}"
    

class NPMPackage(ABC):
    name: str

    @staticmethod
    def extra_actions() -> None:
        pass

    @abstractstaticmethod
    @staticmethod
    def get_package() -> None:
        pass

    @abstractclassmethod
    @classmethod
    def get_full_name(cls) -> str:
        pass
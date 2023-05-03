from typing import List, Dict


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
        return f"{cls.name} ({cls.cdn_provider.name})"

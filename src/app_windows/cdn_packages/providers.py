from .abstract import CDNProvider


class UnPKG(CDNProvider):
    name = "unpkg"
    provider_endpoint = "https://unpkg.com"

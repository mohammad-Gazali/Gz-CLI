from core.abstract import CDNProvider


class JsDeliver(CDNProvider):
    name = "jsdelivr"
    provider_endpoint = "https://cdn.jsdelivr.net/npm"


class UnPKG(CDNProvider):
    name = "unpkg"
    provider_endpoint = "https://unpkg.com"

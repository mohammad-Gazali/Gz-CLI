from .abstract import CDNPackage
from .providers import UnPKG
from .constants import (
    BOOTSTRAP_PATHS,
    PRELINE_PATHS,
    HTMX_PATHS,
    APLINE_PATHS,
    FLOWBITE_PATHS,
    AXIOS_PATHS,
)


class BootstrapUnPKG(CDNPackage):
    name = "bootstrap"
    cdn_provider = UnPKG
    need_tailwind = False
    paths = BOOTSTRAP_PATHS


class PrelineUnPKG(CDNPackage):
    name = "preline"
    cdn_provider = UnPKG
    need_tailwind = True
    paths = PRELINE_PATHS


class HTMXUnPKG(CDNPackage):
    name = "htmx.org"
    cdn_provider = UnPKG
    need_tailwind = False
    paths = HTMX_PATHS


class AlpineUnPKG(CDNPackage):
    name = "alpinejs"
    cdn_provider = UnPKG
    need_tailwind = False
    paths = APLINE_PATHS


class FlowbiteUnPKG(CDNPackage):
    name = "flowbite"
    cdn_provider = UnPKG
    need_tailwind = True
    paths = FLOWBITE_PATHS


class AxiosUnPKG(CDNPackage):
    name = "axios"
    cdn_provider = UnPKG
    need_tailwind = False
    paths = AXIOS_PATHS

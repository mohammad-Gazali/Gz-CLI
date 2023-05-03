from core.abstract import CDNPackage
from core.providers import UnPKG
from core.constants import BOOTSTRAP_PATHS, PRELINE_PATHS, HTMX_PATHS, APLINE_PATHS



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
    name = "HTMX"
    cdn_provider = UnPKG
    need_tailwind = False
    paths = HTMX_PATHS


class AlpineUnPkg(CDNPackage):
    name = "alpine"
    cdn_provider = UnPKG
    need_tailwind = False
    paths = APLINE_PATHS
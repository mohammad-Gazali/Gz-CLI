from core import packages
from core.abstract import CDNPackage



PACKAGES_LIST: list[CDNPackage] = [
    packages.BootstrapJsDeliver,
    packages.BootstrapUnPKG,
    packages.PrelineJsDeliver,
    packages.PrelineUnPKG,
    packages.HTMXJsDeliver,
    packages.HTMXUnPKG,
]

PACKAGES_LIST_JS_DELIVER: list[CDNPackage] = [
    packages.BootstrapJsDeliver,
    packages.PrelineJsDeliver,
    packages.HTMXJsDeliver,
]

PACKAGES_LIST_UNPKG: list[CDNPackage] = [
    packages.BootstrapUnPKG,
    packages.PrelineUnPKG,
    packages.HTMXUnPKG,
]
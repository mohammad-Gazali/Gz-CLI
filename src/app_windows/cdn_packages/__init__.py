from . import packages
from .abstract import CDNPackage


PACKAGES_LIST: list[CDNPackage] = [
    packages.BootstrapUnPKG,
    packages.PrelineUnPKG,
    packages.HTMXUnPKG,
    packages.AlpineUnPKG,
    packages.FlowbiteUnPKG,
]

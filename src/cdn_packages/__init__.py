from cdn_packages import packages
from core.abstract import CDNPackage


PACKAGES_LIST: list[CDNPackage] = [
    packages.BootstrapUnPKG,
    packages.PrelineUnPKG,
    packages.HTMXUnPKG,
    packages.AlpineUnPKG,
    packages.FlowbiteUnPKG,
]
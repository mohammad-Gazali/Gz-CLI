from app_windows.cdn_packages.abstract import CDNPackage
from app_windows.npm_packages.tailwindcss import TailwindCSS
import requests
import os
import re


class SysytemControlWithPackage:
    def __init__(self, package: CDNPackage) -> None:
        self.__package = package
        self.is_tailwindcss = False

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, new_package):
        self.__package = new_package

    @staticmethod
    def make_folder(*paths):
        result_path = os.path.join(*paths)
        try:
            os.makedirs(result_path)
        except FileExistsError:
            pass

    def get_package(self, output_folder: str):
        if not self.is_tailwindcss and self.__package.need_tailwind:
            self.is_tailwindcss = True
            TailwindCSS.get_tailwindcss()

        for path in self.__package.paths:
            url_path = path["url_path"]
            output_path = path["output_path"]

            output_path_without_file = re.split(r"\\|\/", output_path)[:-1]

            self.make_folder(output_folder, *output_path_without_file)

            with open(os.path.join(output_folder, output_path), "wb") as file:
                data = requests.get(f"{self.__package.cdn_url()}/{url_path}").content
                file.write(data)

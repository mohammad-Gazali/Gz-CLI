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

    @staticmethod
    def add_to_tailwind_config_file(package):
        with open("tailwind.config.js", "r+") as file:
            file_content = file.read()

            start_index = file_content.find("plugins: [") + 10

            file_content_list = list(file_content)

            if file_content[start_index] == "]":
                file_content_list.insert(
                    start_index, f'\n\t\trequire("{package}/plugin"),\n\t'
                )

            elif file_content[start_index] == "\n":
                file_content_list.insert(start_index, f'\n\t\trequire("{package}/plugin"),\t')

            new_content = "".join(file_content_list)

            # reset file pointer to beginning of file
            file.seek(0)

            file.write(new_content)

    def get_package(self, output_folder: str):
        if not self.is_tailwindcss and self.__package.need_tailwind:
            self.is_tailwindcss = True
            TailwindCSS.get_tailwindcss()
            os.system(f"npm i {self.__package.name}")
            self.add_to_tailwind_config_file(self.__package.name)

        for path in self.__package.paths:
            url_path = path["url_path"]
            output_path = path["output_path"]

            output_path_without_file = re.split(r"\\|\/", output_path)[:-1]

            self.make_folder(output_folder, *output_path_without_file)

            with open(os.path.join(output_folder, output_path), "wb") as file:
                data = requests.get(f"{self.__package.cdn_url()}/{url_path}").content
                file.write(data)

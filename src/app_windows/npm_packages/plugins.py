import os

try:
    from tailwindcss import TailwindCSS
except ModuleNotFoundError:
    from app_windows.npm_packages.tailwindcss import TailwindCSS


class TailwindPlugin:
    name: str

    @classmethod
    def get_full_name(cls) -> str:
        package_identifier = cls.name.split("/")[-1]
        return f"tailwind plugin {package_identifier}"

    @classmethod
    def get_package(cls):
        os.system(f"npm install -D {cls.name}")
        cls.add_to_config_file()

    @classmethod
    def add_to_config_file(cls):
        with open("tailwind.config.js", "r+") as file:
            file_content = file.read()

            start_index = file_content.find("plugins: [") + 10

            file_content_list = list(file_content)

            if file_content[start_index] == "]":
                file_content_list.insert(
                    start_index, f'\n\t\trequire("{cls.name}"),\n\t'
                )

            elif file_content[start_index] == "\n":
                file_content_list.insert(start_index, f'\n\t\trequire("{cls.name}"),\t')

            else:
                TailwindCSS.add_config_file()
                file_content_list.insert(
                    start_index, f'\n\t\trequire("{cls.name}"),\n\t'
                )

            new_content = "".join(file_content_list)

            # reset file pointer to beginning of file
            file.seek(0)

            file.write(new_content)


# ? ======= Plugins =======


class TailwindFormsPlugin(TailwindPlugin):
    name = "@tailwindcss/forms"


class TailwindTypographyPlugin(TailwindPlugin):
    name = "@tailwindcss/typography"


class TailwindAspectRatioPlugin(TailwindPlugin):
    name = "@tailwindcss/aspect-ratio"


class TailwindContainerQueriesPlugin(TailwindPlugin):
    name = "@tailwindcss/container-queries"


class DaisyuiPlugin(TailwindPlugin):
    name = "daisyui"


PLUGINS_LIST: list[TailwindPlugin] = [
    TailwindFormsPlugin,
    TailwindTypographyPlugin,
    TailwindAspectRatioPlugin,
    TailwindContainerQueriesPlugin,
    DaisyuiPlugin,
]

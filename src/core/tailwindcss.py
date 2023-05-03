import os


# TODO: installing plugins

class TailwindCSS:
    @staticmethod
    def add_watch_script():
        with open("package.json", "r+") as file:
            # Read the existing lines into a list
            lines = file.readlines()

            # Delete the last line in the package.json file
            del lines[-2]
            del lines[-1]

            # Adding "watch" script for watching tailwindcss file
            lines.append("\t},\n")
            lines.append('\t"scripts": {\n')
            lines.append(
                '\t\t"watch": "tailwindcss -i ./static/css/tailwind-input.css -o ./static/css/tailwind-output.css --watch"\n'
            )
            lines.append("\t}\n")
            lines.append("}")

            # Move the file pointer back to the beginning of the file
            file.seek(0)

            # Overwrite the file with the modified list of lines
            file.writelines(lines)

    @staticmethod
    def add_tailwind_files():

        css_path = os.path.join("static", "css")

        try:
            os.makedirs(css_path)
        except FileExistsError:
            pass

        input_path = os.path.join(css_path, "tailwind-input.css")
        output_path = os.path.join(css_path, "tailwind-output.css")

        with open(input_path, "w") as file:
            file.writelines(
                [
                    "@tailwind base;\n",
                    "@tailwind components;\n",
                    "@tailwind utilities;\n",
                ]
            )

        with open(output_path, "w"):
            pass

    @staticmethod
    def add_config_file():
        with open("tailwind.config.js", "w") as file:
            file.writelines(
                [
                    "/** @type {import('tailwindcss').Config} */\n",
                    "module.exports = {\n",
                    '\tdarkMode: "class",\n',
                    "\tcontent: [\n",
                    '\t\t"./templates/**/*.{html}",\n',
                    "\t],\n",
                    "\ttheme: {\n",
                    "\t\textend: {},\n",
                    "\t},\n",
                    "\tplugins:[]\n",
                    "}",
                ]
            )

    @staticmethod
    def install_tailwind():
        os.system("npm install -D tailwindcss postcss autoprefixer")
        os.system("npx tailwindcss init -p")

    @staticmethod
    def get_tailwindcss():
        TailwindCSS.install_tailwind()
        TailwindCSS.add_watch_script()
        TailwindCSS.add_tailwind_files()
        TailwindCSS.add_config_file()
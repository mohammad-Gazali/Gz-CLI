import os
from django.core.management.utils import get_random_secret_key


try:
    from .constants import GITIGNORE_FILE_CONTENT, README_FILE_CONTENT
except ImportError:
    from constants import GITIGNORE_FILE_CONTENT, README_FILE_CONTENT


def edit_settings_file(project_name):

    settings_path = os.path.join(project_name, "settings.py")

    with open(settings_path, "r+") as file:
        file_content_lines = file.readlines()

        STATIC_URL_line_index = None
        INITIAL_ALLOWED_HOSTS_line_index = None
        TEMPLATE_DIRS_line_index = None
        SECRET_KEY_line_index = None
        DEBUG_line_index = None
        IMPORT_line_index = None

        for index, line in enumerate(file_content_lines):

            if line.count("import Path") > 0:
                IMPORT_line_index = index

            if line.count("SECRET_KEY") > 0:
                SECRET_KEY_line_index = index

            if line.count("DEBUG") > 0:
                DEBUG_line_index = index

            if line.count("ALLOWED_HOSTS = []") > 0:
                INITIAL_ALLOWED_HOSTS_line_index = index

            if line.count("STATIC_URL") > 0:
                STATIC_URL_line_index = index

            if line.count("'DIRS'") > 0 or line.count('"DIRS"') > 0:
                TEMPLATE_DIRS_line_index = index

        # ? ==================== start editings =============================

        #! IMPORTANT NOTE: the order of if statements below matter
        #! if we change the order then the indexes we find in the for loop above will be wrong

        if TEMPLATE_DIRS_line_index is not None:
            file_content_lines[
                TEMPLATE_DIRS_line_index
            ] = '\t\t"DIRS": ["templates"],\n'

        if SECRET_KEY_line_index is not None:
            file_content_lines[
                SECRET_KEY_line_index
            ] = f'SECRET_KEY = os.environ.get("SECRET_KEY", default="django-insecure-{get_random_secret_key()}")\n'

        if DEBUG_line_index is not None:
            file_content_lines[
                DEBUG_line_index
            ] = 'DEBUG = os.environ.get("DEBUG", default="False") == "True"\n'

        if STATIC_URL_line_index is not None:
            first_part = file_content_lines[:STATIC_URL_line_index]
            second_part = file_content_lines[STATIC_URL_line_index + 1 :]
            new_part = [
                "\n# static files configurations\n",
                file_content_lines[STATIC_URL_line_index],
                'STATICFILES_DIRS = [BASE_DIR / "static"]\n',
                'STATIC_ROOT = BASE_DIR / "staticfiles"\n',
                "\n# media files configurations\n",
                'MEDIA_URL = "/media/"\n',
                'MEDIA_ROOT = BASE_DIR / "media"\n\n',
            ]

            file_content_lines = first_part + new_part + second_part

        if INITIAL_ALLOWED_HOSTS_line_index is not None:
            first_part = file_content_lines[:INITIAL_ALLOWED_HOSTS_line_index]
            second_part = file_content_lines[INITIAL_ALLOWED_HOSTS_line_index + 1 :]

            new_part = [
                "ALLOWED_HOSTS = [\n",
                '\t"127.0.0.1",\n',
                '\t"localhost",\n',
                "]\n",
                "\n",
                "if not DEBUG:\n",
                '\tALLOWED_HOSTS += [os.environ.get("ALLOWED_HOST")]\n',
            ]

            file_content_lines = first_part + new_part + second_part

        if IMPORT_line_index is not None:
            file_content_lines.insert(IMPORT_line_index + 1, "import os")

        # ? ==================== end editings =============================

        # getting rid of extra lines before "from pathlib import Path"
        file_content_lines = file_content_lines[IMPORT_line_index:]

        file.seek(0)

        file.writelines(file_content_lines)

        # make "media" folder
        try:
            os.mkdir("media")
        except FileExistsError:
            pass

        # make "templates" folder
        try:
            os.mkdir("templates")
        except FileExistsError:
            pass


def edit_urls_file(project_name):
    urls_path = os.path.join(project_name, "urls.py")

    with open(urls_path, "r+") as file:
        file_content_lines = file.readlines()

        import_line_index = None

        for index, line in enumerate(file_content_lines):
            if line == '"""\n' and index != 0:
                import_line_index = index + 1
                break

        if import_line_index is not None:
            file_content_lines = file_content_lines[import_line_index:]

            # file_content_lines[1] = "from django.urls import path\n"
            # adding include function to imports
            file_content_lines[1] = file_content_lines[1][:-1] + ", include\n"

            # # adding two new imports
            file_content_lines.insert(2, "\n")
            file_content_lines.insert(2, "\n")
            file_content_lines.insert(2, "from django.conf.urls.static import static\n")
            file_content_lines.insert(2, "from django.conf import settings\n")

            file_content_lines.append("\n")
            file_content_lines.append("if settings.DEBUG:\n")
            file_content_lines.append(
                "\turlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n"
            )

        file.seek(0)

        file.writelines(file_content_lines)


def edit_wsgi_file(project_name):

    wsgi_path = os.path.join(project_name, "wsgi.py")

    with open(wsgi_path, "r+") as file:
        file_content_lines = file.readlines()

        import_line_index = None

        for index, line in enumerate(file_content_lines):
            if line.count("get_wsgi_application") > 0:
                import_line_index = index
                break

        if import_line_index is not None:

            file_content_lines.insert(import_line_index, "import dotenv\n")

            file_content_lines.insert(
                import_line_index + 2,
                "dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))\n",
            )
            file_content_lines.insert(import_line_index + 2, "\n")

        file.seek(0)

        file.writelines(file_content_lines)


def add_gitignore_file():
    with open(".gitignore", "w") as file:
        file.write(GITIGNORE_FILE_CONTENT)


def add_vscode_workspace():

    os.mkdir(".vscode")

    workspace_path = os.path.join(".vscode", "settings.json")

    with open(workspace_path, "w") as file:
        file.writelines(
            [
                "{\n",
                '\t"python.analysis.typeCheckingMode": "basic",\n'
                '\t"python.analysis.autoImportCompletions": true,\n',
                '\t"python.analysis.packageIndexDepths": [\n',
                "\t\t{\n",
                '\t\t\t"name": "django",\n',
                '\t\t\t"depth": 4\n',
                "\t\t},\n",
                "\t],\n",
                "}\n",
            ]
        )


def add_readme_file():
    with open("README.md", "w") as file:
        file.write(README_FILE_CONTENT)


def add_env_file():
    with open(".env", "w") as env_file:
        env_file.writelines(
            [
                "# project configurations \n",
                f"SECRET_KEY=django-insecure-{get_random_secret_key()}\n",
                "DEBUG=True\n",
                "WEBSITE_URL=127.0.0.1:8000\n",
                "ALLOWED_HOST=127.0.0.1\n",
            ]
        )

    with open(".env.example", "w") as env_example_file:
        env_example_file.writelines(
            [
                "# project configurations \n",
                "SECRET_KEY=\n",
                "DEBUG=\n",
                "WEBSITE_URL=\n",
                "ALLOWED_HOST=\n",
            ]
        )


def add_git_repo():
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "initial commit"')


def env_file_configurations():
    with open("manage.py", "r+") as file:
        file_content_lines = file.readlines()

        sys_import_line_index = None
        new_line_index = None

        for index, line in enumerate(file_content_lines):
            if line.count("import sys") > 0:
                sys_import_line_index = index

            if line.count("Run administrative tasks") > 0:
                new_line_index = index + 2

        if sys_import_line_index is not None:
            file_content_lines.insert(sys_import_line_index + 1, "import dotenv")

        if new_line_index is not None:
            file_content_lines.insert(new_line_index, "    dotenv.read_dotenv()\n")

        file.seek(0)

        file.writelines(file_content_lines)

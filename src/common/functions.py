import os

try:
    from .constants import GITIGNORE_FILE_CONTENT
except ImportError:
    from constants import GITIGNORE_FILE_CONTENT


def edit_settings_file(project_name):

    settings_path = os.path.join(project_name, "settings.py")

    with open(settings_path, "r+") as file:
        file_content_lines = file.readlines()

        STATIC_URL_line_index = None

        for index, line in enumerate(file_content_lines):
            if line.count("STATIC_URL") > 0:
                STATIC_URL_line_index = index
                break

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

        file.seek(0)

        file.writelines(file_content_lines)

        # make "media" folder
        try:
            os.mkdir("media")
        except FileExistsError:
            pass


def edit_urls_file(project_name):
    urls_path = os.path.join(project_name, "urls.py")

    with open(urls_path, "r") as file:
        file_content_lines = file.readlines()

        import_line_index = None

        for index, line in enumerate(file_content_lines):
            if line == '"""\n' and index != 0:
                import_line_index = index + 1
                break

        if import_line_index is not None:
            new_content = file_content_lines[import_line_index:]    

            # new_content[1] = "from django.urls import path\n"
            # adding include function to imports
            new_content[1] = new_content[1][:-1] + ", include\n"

            # # adding two new imports
            new_content.insert(2, "\n")
            new_content.insert(2, "\n")
            new_content.insert(2, "from django.conf.urls.static import static\n")
            new_content.insert(2, "from django.conf import settings\n")

            new_content.append("\n")
            new_content.append("if settings.DEBUG:\n")
            new_content.append(
                "\turlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n"
            )

            with open(urls_path, "w") as writeable_file:
                writeable_file.writelines(new_content)


def add_gitignore_file():
    with open(".gitignore", "w") as file:
        file.write(GITIGNORE_FILE_CONTENT)
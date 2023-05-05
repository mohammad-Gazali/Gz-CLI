from django.core.management import call_command
import os


def common_actions_func():
    project_name = "project_core"

    # create django project
    call_command("startproject", project_name, ".")

    settings_path = os.path.join(project_name, "settings.py")

    # editing settings.py file
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

        try:
            os.mkdir("media")
        except FileExistsError:
            pass

    # TODO: editing urls.py for static files

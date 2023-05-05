from django.core.management import call_command

try:
    from .functions import edit_settings_file, edit_urls_file, add_gitignore_file
except ImportError:
    from functions import edit_settings_file, edit_urls_file, add_gitignore_file



def common_actions_func(project_name):

    # create django project
    call_command("startproject", project_name, ".")

    # edit settings.py
    edit_settings_file(project_name)

    # edit urls.py
    edit_urls_file(project_name)

    # add .gitignore file
    add_gitignore_file()

    # TODO: add README.md file

    # TODO: add configurations to .env file

    # TODO: add .env file
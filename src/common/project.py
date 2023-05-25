from django.core.management import call_command

try:
    from .functions import (
        edit_settings_file,
        edit_urls_file,
        edit_wsgi_file,
        add_gitignore_file,
        add_vscode_workspace,
        add_readme_file,
        add_env_file,
        add_git_repo,
        env_file_configurations,
    )
except ImportError:
    from functions import (
        edit_settings_file,
        edit_urls_file,
        edit_wsgi_file,
        add_gitignore_file,
        add_vscode_workspace,
        add_readme_file,
        add_env_file,
        add_git_repo,
        env_file_configurations,
    )


def common_actions_func(project_name: str, workspace: bool, git: bool):

    # create django project
    call_command("startproject", project_name, ".")

    # edit settings.py
    edit_settings_file(project_name)

    # edit urls.py
    edit_urls_file(project_name)

    # edit wsgi.py
    edit_wsgi_file(project_name)

    # add .gitignore file
    add_gitignore_file()

    # add README.md file
    add_readme_file()

    # add .env file
    add_env_file()

    # add configurations for .env file
    env_file_configurations()

    # ? ========= Optional Configurations =========

    # add .vscode for workspace configurations
    if workspace:
        add_vscode_workspace()

    # add init git
    if git:
        add_git_repo()

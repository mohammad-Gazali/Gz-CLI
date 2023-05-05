from management.controller import SysytemControlWithPackage
from common.project import common_actions_func
from app_windows.cdn_pkgs_window import cdn_packages_main, cdn_choices_menu
from app_windows.tailwind_plugins_window import (
    tailwind_plugins_main,
    tailwind_plugins_choices_menu,
)
import curses


def main_app_function():

    # ? =================  Collect Data ====================

    # * 1. cdn_packages
    cdn_user_choices_indexes = curses.wrapper(cdn_packages_main)
    cdn_user_choices = [cdn_choices_menu[i][1] for i in cdn_user_choices_indexes]

    # * 2. tailwind_plugins
    tailwind_plugins_user_choices_indexes = curses.wrapper(tailwind_plugins_main)
    tailwind_plugins_user_choices = [
        tailwind_plugins_choices_menu[i][1]
        for i in tailwind_plugins_user_choices_indexes
    ]

    # ? ================ Actions ===========================

    # * 1. cdn_packages
    if cdn_user_choices:
        controller = SysytemControlWithPackage(cdn_user_choices[0])
        controller.get_package("static")
        if cdn_user_choices[1:]:
            for pkg in cdn_user_choices[1:]:
                controller.package = pkg
                controller.get_package("static")

    # * 2. tailwind_plugins
    if tailwind_plugins_user_choices:
        for choice in tailwind_plugins_user_choices:
            choice.get_package()

    # * 3. common acctions
    common_actions_func()


if __name__ == "__main__":
    main_app_function()

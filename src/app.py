from core import PACKAGES_LIST
from core.controller import SysytemControlWithPackage
from django.core.management import call_command
import curses
import os


CURRENT_PATH = os.getcwd()

choices_menu = [(pkg.get_full_name().capitalize(), pkg) for pkg in PACKAGES_LIST]


def print_menu(stdscr, selected_row_idx, user_choices):
    # Clear the screen
    stdscr.clear()

    stdscr.addstr(
        'Press "Enter" for checking the dependency, then press "d" for confirming your choices'
    )

    # Print the menu items
    for idx, item in enumerate(choices_menu):
        x = 2
        y = idx + 2

        if idx in user_choices and idx == selected_row_idx:
            stdscr.addstr(y, 0, "●")
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(y, x, item[0])
            stdscr.attroff(curses.color_pair(3))

        elif idx in user_choices:
            stdscr.addstr(y, 0, "●")
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x, item[0])
            stdscr.attroff(curses.color_pair(2))

        elif idx == selected_row_idx:
            stdscr.addstr(y, 0, "●")
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, item[0])
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, 0, "●")
            stdscr.addstr(y, x, item[0])

    # Refresh the screen
    stdscr.refresh()


def main(stdscr):
    # Initialize curses
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)

    # Set initial selected row
    current_row = 0

    # Print the menu
    print_menu(stdscr, current_row, [])

    user_choices = []

    while True:
        # Get user input
        key = stdscr.getch()

        # Move the selection based on user input
        if key == curses.KEY_UP and current_row == 0:
            current_row = len(choices_menu) - 1

        elif key == curses.KEY_DOWN and current_row == len(choices_menu) - 1:
            current_row = 0

        elif key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        elif key == curses.KEY_DOWN and current_row < len(choices_menu) - 1:
            current_row += 1

        elif key == ord("\n"):
            if current_row in user_choices:
                user_choices.remove(current_row)
            else:
                user_choices.append(current_row)

        elif key == ord("d"):
            return user_choices

        # Update the menu
        print_menu(stdscr, current_row, user_choices)


if __name__ == "__main__":

    # ? =================  Collect Data ====================

    user_choices_indexes = curses.wrapper(main)

    user_choices = [choices_menu[i][1] for i in user_choices_indexes]



    # ? ================ Actions ===========================

    # packages
    if user_choices:

        controller = SysytemControlWithPackage(user_choices[0])
        controller.get_package("static")

        if user_choices[1:]:
            for pkg in user_choices[1:]:
                controller.package = pkg
                controller.get_package("static")

    # create django project
    call_command("startproject", "project_core", ".")

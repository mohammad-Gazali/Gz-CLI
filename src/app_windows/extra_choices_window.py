import curses


extra_choices_menu = [
    "adding vscode workspace configurations (you need to have git in your machine)",
    "initializing git repository"
]


def print_menu(stdscr, selected_row_idx, user_choices):
    # Clear the screen
    stdscr.clear()

    stdscr.addstr(
        'Press "Enter" for checking the extra choice, then press "d" for confirming your choices'
    )

    # Print the menu items
    for idx, item in enumerate(extra_choices_menu):
        x = 2
        y = idx + 2

        if idx in user_choices and idx == selected_row_idx:
            stdscr.addstr(y, 0, "●")
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(y, x, item)
            stdscr.attroff(curses.color_pair(3))

        elif idx in user_choices:
            stdscr.addstr(y, 0, "●")
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x, item)
            stdscr.attroff(curses.color_pair(2))

        elif idx == selected_row_idx:
            stdscr.addstr(y, 0, "●")
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, item)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, 0, "●")
            stdscr.addstr(y, x, item)

    # Refresh the screen
    stdscr.refresh()


def extra_main(stdscr):
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
            current_row = len(extra_choices_menu) - 1

        elif (
            key == curses.KEY_DOWN
            and current_row == len(extra_choices_menu) - 1
        ):
            current_row = 0

        elif key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        elif (
            key == curses.KEY_DOWN
            and current_row < len(extra_choices_menu) - 1
        ):
            current_row += 1

        elif key in [ord("\n"), ord(" ")]:
            if current_row in user_choices:
                user_choices.remove(current_row)
            else:
                user_choices.append(current_row)

        elif key == ord("d"):
            return user_choices

        # Update the menu
        print_menu(stdscr, current_row, user_choices)

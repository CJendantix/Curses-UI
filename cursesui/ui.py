import curses
from typing import Callable
from curses import panel as cpanel
from .selector import dict_select
from .common import IndexedDict, default_item_display
from .actions import run_function, select, edit


def dict_ui(
    base_window: curses.window,
    dictionary: dict,
    item_display: Callable[
        [tuple[str, dict], bool], tuple[str, int]
    ] = default_item_display,
):
    base_panel = cpanel.new_panel(base_window)

    while True:
        base_window.clear()
        base_window.refresh()

        item = dict_select(base_window, IndexedDict(dictionary), item_display)
        functionality = item[1]["functionality"]

        if functionality == "quit":
            break
        elif functionality == "run_function":
            run_function(item[1])
        elif functionality == "select":
            dictionary[item[0]]["value"] = select(
                base_window, item[1]["options"], item_display
            )
        elif functionality == "edit":
            dictionary[item[0]]["value"] = edit(base_window, item)
        elif functionality == "sub_menu":
            dict_ui(base_window, item[1]["menu"])

    base_panel.hide()


def selection_ui(
    base_window: curses.window,
    options: dict,
    item_display: Callable[
        [tuple[str, dict], bool], tuple[str, int]
    ] = default_item_display,
) -> str:
    base_panel = cpanel.new_panel(base_window)
    value = select(base_window, options, item_display)
    base_panel.hide()
    return value


def editor_ui(
    base_window: curses.window,
    name: str,
    value: str = "",
    validator: Callable[[str], bool] = lambda x: True,
    allowed_human_readable: str = "",
) -> str:
    base_panel = cpanel.new_panel(base_window)
    value = edit(
        base_window,
        (
            name,
            {
                "value": value,
                "validator": validator,
                "allowed_human_readable": allowed_human_readable,
            },
        ),
    )
    base_panel.hide()
    return value

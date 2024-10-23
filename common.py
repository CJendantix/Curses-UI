import collections
import curses

class IndexedDict(collections.OrderedDict):
    def from_index(self, index: int) -> tuple:
        return list(self.items())[index]

class SpecialKeys():
    Enter = 10
    Quit = ord('q')

class DefaultKeymaps():
    View = {
        "up": [curses.KEY_UP],
        "down": [curses.KEY_DOWN],
        "quit": [SpecialKeys.Quit],
        "action": [SpecialKeys.Enter]
    }
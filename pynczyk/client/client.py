import curses
import logging
from curses.textpad import Textbox, rectangle

from pynczyk.core import Config, Status

logger: logging.Logger = logging.getLogger(__name__)


class App:
    _running: bool = False
    _screen: curses.window

    def _run(self) -> Status:
        self._running = True
        usr_idx: int = 0
        curses.initscr()
        center_x = curses.COLS // 2
        center_y = curses.LINES // 2
        self._screen = curses.newwin(2, 10, center_y, center_x)
        curses.curs_set(0)
        while True:
            self._screen.clear()
            if usr_idx == 0:
                self._screen.addstr(0, 0, "Opcja1", curses.A_REVERSE)
                self._screen.addstr(1, 0, "Opcja2")
            else:
                self._screen.addstr(0, 0, "Opcja1")
                self._screen.addstr(1, 0, "Opcja2", curses.A_REVERSE)
                # self._screen.addstr(0, 0, "Opcja1")
                # self._screen.addstr(1, 0, "Opcja2", curses.A_REVERSE)
            self._screen.keypad(True)
            user_input: int = self._screen.getch()
            self._screen.refresh()
            if user_input == ord("q"):
                self._running = False
                break
            if user_input in {curses.KEY_UP, curses.KEY_DOWN}:
                usr_idx = 0 if usr_idx == 1 else 1
                logger.info("User selected option: %s", usr_idx)

        return Status.OK


class Client(App):
    def __init__(self, config: Config = Config()):
        logger.info("Initializing client with config: %s", config)

        self.config = config

    def run(self) -> Status:
        logger.info("Running client %s", self.config.name)
        self._run()

        return Status.OK

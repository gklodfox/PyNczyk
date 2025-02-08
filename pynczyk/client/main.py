import curses
import logging

from pynczyk import Config, Status

logger: logging.Logger = logging.getLogger(__name__)


class App:
    _running: bool = False
    _screen: curses.window

    def run(self) -> Status:
        self._running = True
        self._screen = curses.initscr()
        self._screen = curses.initscr()

        return Status.OK


class Client:
    def __init__(self, config: Config = Config()):
        logger.info("Initializing client with config: %s", config)

        self.config = config

    def run(self) -> Status:
        logger.info("Running client %s", self.config.name)
        screen = curses.initscr()
        screen.refresh()

        return Status.OK

import logging

from pynczyk import Config, Status

logger: logging.Logger = logging.getLogger(__name__)


class Client:
    def __init__(self, config: Config = Config()):
        logger.info("Initializing client with config: %s", config)

        self.config = config

    def run(self) -> Status:
        logger.info("Running client %s", self.config.name)

        return Status.OK

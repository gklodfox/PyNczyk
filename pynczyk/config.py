import logging

logger: logging.Logger = logging.getLogger(__name__)


class Config:
    def __init__(self, idx: int = 0, name: str = "client"):
        logger.info("Initializing default config")

        self.idx = idx
        self.name = name

    def __repr__(self):
        return f"Config(id={self.idx}, name={self.name})"

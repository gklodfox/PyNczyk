import sys
import logging

from pynczyk.client import Client
from pynczyk.core import Status

logger: logging.Logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def run_client() -> Status:
    logger.info("Starting client")
    client: Client = Client()

    logger.info(client.config)

    return client.run()


def run_server() -> Status:
    return NotImplemented

    # logger.info("Starting server")
    #
    # return Status.OK

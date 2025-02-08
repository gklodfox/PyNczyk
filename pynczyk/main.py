import logging

from pynczyk import Client, Status

logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


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

# Logging Means :- Capture details, which are useful for debugging.
# and show the user about execution of the  prograam and other details.

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("Test print logs")
    LOGGER.warning("Test print logs")
    LOGGER.error("Test print logs")
    LOGGER.critical("Test print logs")
    LOGGER.debug("Test print logs")
    LOGGER.log(logging.INFO, "Test print logs")
    
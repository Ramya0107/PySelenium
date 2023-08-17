# Logging - we can add logs for failures, information, error, warning

import logging


def test_print_logs():
    logger = logging.getLogger(__name__)

    # Intentional logging
    logger.info("This is information logs")
    logger.warning("This is information logs")
    logger.error("This is information logs")
    logger.critical("This is information logs")

# if log_cli_level = ERROR in pytest.ini -> o/p ERROR , CRITICAL displayed
# if log_cli_level = INFO in pytest.ini -> o/p INFO, WARNING, ERROR , CRITICAL displayed


# CRITICAL: The highest severity level. Represents critical errors that might lead to application crashes or major
# failures.
# ERROR: Represents errors that impact the normal flow of the application but might not cause a crash.
# WARNING: Represents warnings about potential issues or unexpected behavior that might lead to problems.
# INFO: General informational messages about the progress or state of the application.
# DEBUG: Detailed debugging messages that can help you diagnose issues or understand the internal workings of the
# application.
# NOTSET: This level is used when you want to include all log messages regardless of their level.

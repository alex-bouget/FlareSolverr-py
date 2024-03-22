import logging


def setup_logger(log_level: str) -> logging.Logger:
    logger = logging.getLogger("flaresolverr")
    logger.setLevel(log_level)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

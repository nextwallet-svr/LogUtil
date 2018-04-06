import json
import logging.config
import os

def setup_logging(default_path = "logging.json", default_level = logging.DEBUG, env_key = "LOG_CFG"):
    path = default_path
    value = os.getenv(env_key,None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path,"r") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level = default_level)


def debug(msg, *args, **kwargs):
    logging.debug(msg, *args, **kwargs)

def error(msg, *args, **kwargs):
    logging.error(msg, *args, **kwargs)

def info(msg, *args, **kwargs):
    logging.info(msg, *args, **kwargs)

def fatal(msg, *args, **kwargs):
    logging.critical(msg, *args, **kwargs)
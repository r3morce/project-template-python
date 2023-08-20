import argparse
import logging
import os

from dotenv import load_dotenv

load_dotenv()


from modules.output import print_hello

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--debug",
    action="store_true",
    default=False,
    help="Enable debug mode and debug logging",
)

args = parser.parse_args()
DEBUG = args.debug


if DEBUG:
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Debug mode enabled")


def main():
    logging.info("Script started")
    print_hello()
    logging.info("Script ended")


if __name__ == "__main__":
    main()

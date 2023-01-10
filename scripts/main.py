# Imports
from backend import get_logger
from pathlib import Path


# Variables
logger = get_logger(Path(__file__).name)


# Functions and classes
def main() -> None:
    logger.log('Started main!')
    logger.log('Completed main!')
    pass


if __name__ == "__main__":
    main()

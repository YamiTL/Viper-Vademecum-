import logging


def main():
    logging.basicConfig(level=logging.DEBUG)

    logging.debug("This is a debug message!")
    logging.info("This is an info message!")
    logging.warning("This is a warning!")
    logging.error("This is an error message!")
    logging.critical("This is an critical message!")


if __name__ == "__main__":
    main()

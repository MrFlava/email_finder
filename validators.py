from os import path
from argparse import Action

from loguru import logger

from settings import INPUT_DIR


class ValidateInputAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values.endswith((".jpeg", ".png", )):
            logger.error("Got value:", values)

            raise ValueError("Not an image!")

        elif not path.exists(path.join(path.join(INPUT_DIR, values))):
            logger.error("Image does not exist:", values)

            raise ValueError("Image does not exist!")

        setattr(namespace, self.dest, values)


class ValidateOutputAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values.endswith((".txt", )):
            logger.error("Got value:", values)

            raise ValueError("Not a text file!")

        setattr(namespace, self.dest, values)

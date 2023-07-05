import re
import argparse
from typing import Tuple
from os import path, getpid, remove

import cv2
import pytesseract
from PIL import Image

from settings import INPUT_DIR, OUTPUT_DIR, PREPROCESS, EMAIL_REGEX


def get_fields_from_terminal() -> Tuple[str, str]:
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input",  help="input image", required=True)
    argParser.add_argument("-o", "--output", help="output document", required=True)
    args = argParser.parse_args()

    return args.input, args.output


def process_the_image(image_path: str) -> str:
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if PREPROCESS == "thresh":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    elif PREPROCESS == "blur":
        gray = cv2.medianBlur(gray, 3)

    filename = f"{getpid()}.png"
    cv2.imwrite(filename, gray)

    return filename


def process_tempfile(filename: str) -> str:
    text = pytesseract.image_to_string(Image.open(filename))
    remove(filename)

    return text


def write_the_output(found_emails: list, output_file_path: str):
    with open(output_file_path, "w") as output_file:
        for email in found_emails:
            output_file.write(f"{email}\n")


def run():

    input_filename, output_filename = get_fields_from_terminal()

    input_file_path = path.join(INPUT_DIR, input_filename)
    output_file_path = path.join(OUTPUT_DIR, output_filename)

    image_path = path.join(input_file_path)
    temp_file_name = process_the_image(image_path)

    text = process_tempfile(temp_file_name)
    emails = re.findall(EMAIL_REGEX, text)
    write_the_output(emails, output_file_path)


if __name__ == "__main__":
    run()

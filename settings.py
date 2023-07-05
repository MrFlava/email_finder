from os import path

BASE_DIR = path.abspath(path.dirname(__file__))
INPUT_DIR = path.join(BASE_DIR, "image")
OUTPUT_DIR = path.join(BASE_DIR, "output")
PREPROCESS = "thresh"
EMAIL_REGEX = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"

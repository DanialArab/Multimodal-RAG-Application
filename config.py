# config.py
import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, "data")
PDF_PATH = os.path.join(DATA_DIR, "attention_paper.pdf")
OUTPUT_DIR = os.path.join(DATA_DIR, "processed")


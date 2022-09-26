import shutil
import os

def clean_data():
    if os.path.exists("data"):
        shutil.rmtree("data")
        os.mkdir("data")
        os.mkdir("data/Lyrics")
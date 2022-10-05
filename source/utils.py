import shutil
import os

def clean_data():
    print("Cleanning existing data : lyrics and french rappers")
    if os.path.exists("data/Lyrics"):
        shutil.rmtree("data/Lyrics")
        os.mkdir("data/Lyrics")

    if os.path.exists("data/french_rapper.csv"):
        os.remove("data/french_rapper.csv")
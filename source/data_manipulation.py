import os
import pandas as pd
import re
def songs_organisers(folder_artists_path):
    
    df_lyrics = pd.DataFrame(columns=['Artist', 'SongName', 'Lyrics'])
    for fd in os.listdir(folder_artists_path):
        for song in os.listdir(folder_artists_path + "/" + fd):
            with open(folder_artists_path + "/" + fd + "/" + song) as lyric:
                df_lyrics = pd.concat([df_lyrics, pd.DataFrame([[fd, song, lyric.read()]], columns=["Artist", "SongName", "Lyrics"])], ignore_index=True)

    return df_lyrics

def text_cleaning(lyrics):
    """text cleaning 

    Args:
        lyrics (string): one song
    """
    
    # Can be usable
    # Title = lyrics.split("Lyrics")[0][:-1]
    
    lyrics = lyrics.replace(lyrics.split("\n")[0], "")[3:-7]
    lyrics = re.sub("\[.*","", lyrics)
    lyrics = lyrics.replace("\n", ". ")
    lyrics = lyrics.replace("- ", "")
    
    lyrics = re.sub("[.,;!?:()\"]","", lyrics)
    lyrics = re.sub("[0-9]","", lyrics)
    lyrics = re.sub("['‘’]", " ", lyrics)
    lyrics = lyrics.replace("  ", " ")
    lyrics = lyrics.replace("  ", " ")
    lyrics = lyrics.lower()
    return lyrics
import os
import pandas as pd

def songs_organisers(folder_artists_path):
    df_lyrics = pd.DataFrame(columns=['Artist', 'SongName', 'Lyrics'])
    for fd in os.listdir(folder_artists_path):
        for song in os.listdir(folder_artists_path + "/" + fd):
            with open(folder_artists_path + "/" + fd + "/" + song) as lyric:
                df_lyrics = pd.concat([df_lyrics, pd.DataFrame([[fd, song, lyric.read()]], columns=["Artist", "SongName", "Lyrics"])], ignore_index=True)

    return df_lyrics
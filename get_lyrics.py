
# Client id : IJIBPtxdiJzt1O3hUb-29illeuVx9L2nkAnPunspWuURVHhBu6BlyE0lMtr9DrLG
# Client secret : yAmrp7206ebLHjJfVSjYWzxiB6dR5351znssA4ri-f3gyFmhugUCpDX2WPVv51HoYuYDtfT3c-S4mF2NjzI2gw
# Access token : 3Uwh10E3D5poEL5-0rDbLiCKWayTs8sS8fSF0IE6CM5aA4SysSQPMSb0A5LSIGGi

#Assign your Genius.com credentials and select your artist

import lyricsgenius as genius
import os 
geniusCreds = "3Uwh10E3D5poEL5-0rDbLiCKWayTs8sS8fSF0IE6CM5aA4SysSQPMSb0A5LSIGGi"
artist_name = "Alkapote"

os.mkdir("Lyrics/"+artist_name)

#Connect your credentials and chosen artist to the genius object then test the first 5 songs
api = genius.Genius(geniusCreds)
artist = api.search_artist(artist_name, max_songs=5)

for song in artist.songs:
    with open("Lyrics/"+artist_name+'/'+song.title+'.txt', 'w') as f:
        f.write(song.lyrics)
    f.close()

# import pandas as pd
# Artist=pd.read_json("Lyrics_"+artist_name+".json")

# Artist['songs']
# Artist['songs'][5]['lyrics']
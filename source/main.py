import scrapping
import utils
import pandas as pd
import os 
from os import path

def french_rapper_to_csv():
    # EXECUTE FRENCH_RAPPER QUERY ON WIKIDATA AND CONVERT RESULTS TO DATAFRAME AND CSV
    results = scrapping.query_wikidata("source/french_rapper.sparql")

    df = pd.DataFrame(columns=['uri', 'name'])
    d = []

    for rapper in results['results']['bindings']:
        d.append(
            {
                'uri': rapper['rapper']['value'],
                'name': rapper['name']['value']
            }
        )

    df = pd.DataFrame(d)
    print(df.head(10))

    df.to_csv('data/french_rappers.csv', index=False)

def get_feats(song_name, api):
    # GET ALL THE FETURING ARTISTS OF A GIVEN SONG
    feats = scrapping.get_featuring_artists(song_name, api)
    for feat in feats:
        print(feat['name'])

def get_songs(artist_name, genius):
    # GET ALL THE SONGS FOR A GIVEN ARTIST AND WRITE THEIR LYRICS IN TXT FILES
    songs = scrapping.get_songs_of(artist_name, genius)
    for song in songs:
            print(song.title)
            with open("data/Lyrics/"+artist_name+'/'+song.title+'.txt', 'w') as f:
                f.write(song.lyrics)
            f.close()


api, genius = scrapping.connect_genius_api()

# arr = os.listdir()
# print(arr)

utils.clean_data()

french_rapper_to_csv()

artist_name = "Orelsan"
if not path.exists("data/Lyrics/"+artist_name):
    os.mkdir("data/Lyrics/"+artist_name)
get_songs(artist_name, genius)

artist_name = "Gringe"
song_name = "qui dit mieux"
get_feats(song_name +' '+artist_name, api)



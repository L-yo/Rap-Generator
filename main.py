from source.scrapping import *
import source.utils as utils
import pandas as pd
import os 
from os import path
from requests.exceptions import Timeout

def french_rapper_to_csv():
    # EXECUTE FRENCH_RAPPER QUERY ON WIKIDATA AND CONVERT RESULTS TO DATAFRAME AND CSV
    print("Retrieving all french/belgians/swiss rappers : ")
    print("Querying Wikidata.org ...")
    results = query_wikidata("data/queries/french_rapper.sparql")

    df = pd.DataFrame(columns=['uri', 'name'])
    d = []

    for rapper in results['results']['bindings']:
        d.append(
            {
                'uri': rapper['rapper']['value'],
                'name': rapper['name']['value']#.lower()
            }
        )

    df = pd.DataFrame(d)

    print("Saving data to data/french_rappers.csv")
    df.to_csv('data/french_rappers.csv', index=False)

def get_feats(song_name, api):
    # GET ALL THE FETURING ARTISTS OF A GIVEN SONG
    feats = get_featuring_artists(song_name, api)
    for feat in feats:
        print(feat['name'])

def get_songs(artist_name, genius, retries=0):
    # GET ALL THE SONGS FOR A GIVEN ARTIST AND WRITE THEIR LYRICS IN TXT FILES
    try:
        songs = get_songs_of(artist_name, genius)
    except Timeout as e:
        retries += 1
        print("Timeout, retrying again ("+retries+")")
        get_songs(artist_name, genius, retries)


    for song in songs:
            print(song.title)
            with open("data/Lyrics/"+artist_name+'/'+song.title+'.txt', 'w') as f:
                f.write(song.lyrics)
            f.close()

def create_dataset(genius, french_rappers):
    print("Creating the dataset...")
    rappers = pd.read_csv(french_rappers)
    total = rappers['name'].size
    i = 1
    for rapper in rappers["name"]:
        print(rapper + ' ' + str(i) + '/' + str(total))
        if not path.exists("data/Lyrics/"+rapper):
            os.mkdir("data/Lyrics/"+rapper)
        get_songs(rapper, genius)
    
api, genius = connect_genius_api()


# utils.clean_data()
# french_rapper_to_csv()

create_dataset(genius, "data/french_rappers.csv")

#TECHNO TESTS
#
# artist_name = "Orelsan"
# if not path.exists("data/Lyrics/"+artist_name):
#     os.mkdir("data/Lyrics/"+artist_name)
# get_songs(artist_name, genius)

# artist_name = "Gringe"
# song_name = "qui dit mieux"
# get_feats(song_name +' '+artist_name, api)



from source.scrapping import *
import source.utils as utils
import pandas as pd
import os 
from os import path
from requests.exceptions import Timeout

def french_rappers_to_csv():
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
                #'names': rapper['names']['value'],#.lower()
                'labels': rapper['labels']['value'],
                #'genius_id': rapper['genius_id']['value'],
                #'descriptions': rapper['descriptions']['value'],
            }
        )

    df = pd.DataFrame(d)

    print("Saving data to data/french_rappers.csv")
    df.to_csv('data/french_rappers.csv', index=False)

def french_singers_to_csv():
    # EXECUTE FRENCH_SINGER QUERY ON WIKIDATA AND CONVERT RESULTS TO DATAFRAME AND CSV
    print("Retrieving all french/belgians/swiss singers : ")
    print("Querying Wikidata.org ...")
    results = query_wikidata("data/queries/french_singer.sparql")

    df = pd.DataFrame(columns=['uri', 'name'])
    d = []

    for singer in results['results']['bindings']:
        d.append(
            {
                'uri': singer['singer']['value'],
                #'names': singer['names']['value'],#.lower()
                'labels': singer['labels']['value'],
                #'genius_id': singer['genius_id']['value'],
                #'descriptions': singer['descriptions']['value'],
            }
        )

    df = pd.DataFrame(d)

    print("Saving data to data/french_singers.csv")
    df.to_csv('data/french_singers.csv', index=False)

def get_feats(song_name, api):
    # GET ALL THE FETURING ARTISTS OF A GIVEN SONG
    feats = get_featuring_artists(song_name, api)
    for feat in feats:
        print(feat['name'])

def get_songs(artist_name, genius, label, retries=0):
    # GET ALL THE SONGS FOR A GIVEN ARTIST AND WRITE THEIR LYRICS IN TXT FILES
    try:
        songs = get_songs_of(artist_name, genius)
    except Timeout as e:
        retries += 1
        print("Timeout, retrying again ("+retries+")")
        get_songs(artist_name, genius, retries)

    if songs:
        for song in songs:
                title = song.title
                title = title.replace(' ', '_')
                title = title.replace('/', '-')
                print("Haaaan"+ title)
                with open("data/Lyrics/"+label+"/"+artist_name+'/'+title+'.txt', 'w') as f:
                    f.write(song.lyrics)
                f.close()
    else:
        print("Artist or songs not found, sorry")

def create_dataset(genius):
    print("Creating the dataset...")
    rappers = pd.read_csv("data/french_rappers.csv")
    total = rappers['labels'].size
    i = 1
    for rapper in rappers["labels"]:
        print('\n'+rapper + ' ' + str(i) + '/' + str(total))
        if not path.exists("data/Lyrics/"+rapper):
            os.mkdir("data/Lyrics/Rap/"+rapper)
        get_songs(rapper, genius, "Rap")
        i+=1

    singers = pd.read_csv("data/french_singers.csv")
    total = singers['labels'].size
    i = 1
    for singer in singers["labels"]:
        print('\n'+rapper + ' ' + str(i) + '/' + str(total))
        if not path.exists("data/Lyrics/"+singer):
            os.mkdir("data/Lyrics/PaRap/"+singer)
        get_songs(singer, genius, "PaRap")
        i+=1
    
api, genius = connect_genius_api()


utils.clean_data()
french_rappers_to_csv()
french_singers_to_csv()

create_dataset(genius)

#TECHNO TESTS
#
# artist_name = "Orelsan"
# if not path.exists("data/Lyrics/"+artist_name):
#     os.mkdir("data/Lyrics/"+artist_name)
# get_songs(artist_name, genius)

# artist_name = "Gringe"
# song_name = "qui dit mieux"
# get_feats(song_name +' '+artist_name, api)


from genericpath import exists
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import lyricsgenius as genius
from difflib import SequenceMatcher

def query_wikidata(query_name):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    f = open(query_name, 'r') #french_rapper.sparql
    sparql.setQuery(f.read())
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results

def connect_genius_api():
    geniusCreds = ""

    f = open("credentials/genius_api_creds.txt", 'r')
    lines = f.read().split('\n')
    for line in lines:
        if line.split(':')[0] == "Access token ":
            geniusCreds = line.split(':')[1]

    api = genius.API(geniusCreds, timeout=30)
    gen = genius.Genius(geniusCreds, timeout=30)

    return api, gen

def get_featuring_artists(song_name, api):
    song = api.search_songs(song_name)
    feats = song["hits"][0]['result']["featured_artists"]

    return feats

def get_songs_of(artist_name, api):
    #Connect your credentials and chosen artist to the genius object then test the first 5 songs
    artist = api.search_artist(artist_name, max_songs=5)

    ratio = SequenceMatcher(None, artist_name, artist.name).ratio()

    if artist and ratio > 0.5:
        return artist.songs


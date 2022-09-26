# Rap-Generator

Personnal project aiming to manipulate a bunch of technologies with the end goal of generating rap songs

## Setup the environment

We use several python modules that need to be installed 
```
pip install SPARQLWrapper
pip install lyricsgenius
```

## Data scrapping

We get our data from *Wikidata* and *Genius*

From *Wikidata* we retreive individuals who are rappers (_wd:Q2252262_) and speak french (_wd:Q150_)

From *Genius* we retreive all the songs from a given artist and their lyrics and all the other featuring artists 

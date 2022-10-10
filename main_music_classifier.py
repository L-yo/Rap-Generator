from numpy import vectorize
from source.data_manipulation import songs_organisers

import numpy as np

import nltk
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# nltk.download('punkt')

LYRICS_FOLDER = "data/Lyrics"

# Columns = ['Artist', 'SongName', 'Lyrics']
df_songs = songs_organisers(LYRICS_FOLDER)

# Data Cleaning
lyrics_list = np.squeeze(df_songs[["Lyrics"]].to_numpy())

# Vectorizer
vectorizer = TfidfVectorizer()
Lyrics_transformed = vectorizer.fit_transform(lyrics_list)

print(len(vectorizer.get_feature_names_out()))
print(Lyrics_transformed.shape)
print(Lyrics_transformed[0].shape)
print(Lyrics_transformed[0])
print(Lyrics_transformed[0].toarray())

Emb_lyrics = Lyrics_transformed.toarray()
print(Emb_lyrics)
# Building Model